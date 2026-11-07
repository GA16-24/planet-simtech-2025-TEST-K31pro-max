from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

SECONDS_PER_YEAR = 365.0 * 24.0 * 3600.0
HOURS_PER_YEAR = 8760.0


@dataclass(frozen=True)
class CoolingStage:
    total_mw: float
    dry_mw: float
    chiller_mw: float
    electricity_mw: float
    condenser_mw: float
    air_rejection_mw: float


def heating_rate_k_per_year(p: dict[str, Any]) -> float:
    s = p["scenario"]
    return (s["boiling_temperature_c"] - s["initial_temperature_c"]) / s["forecast_years"]


def source_temperature_c(year: float | np.ndarray, p: dict[str, Any]) -> float | np.ndarray:
    s = p["scenario"]
    temperature = s["initial_temperature_c"] + heating_rate_k_per_year(p) * np.asarray(year)
    return np.minimum(temperature, s["source_temperature_cap_c"])


def thermal_capacitance_mw_per_k(p: dict[str, Any], affected_fraction: float | None = None) -> float:
    w = p["water"]
    fraction = p["scenario"]["affected_flow_fraction"] if affected_fraction is None else affected_fraction
    return w["density_kg_m3"] * w["specific_heat_j_kgk"] * w["discharge_m3_s"] * fraction / 1e6


def required_cooling_mw(year: float | np.ndarray, p: dict[str, Any], affected_fraction: float | None = None) -> np.ndarray:
    s = p["scenario"]
    delta = np.maximum(source_temperature_c(year, p) - s["target_temperature_c"], 0.0)
    return thermal_capacitance_mw_per_k(p, affected_fraction) * delta


def dry_outlet_temperature_c(p: dict[str, Any]) -> float:
    plant = p["plant"]
    return plant["summer_design_air_c"] + plant["dry_cooler_approach_k"]


def cooling_stage(year: float, p: dict[str, Any], affected_fraction: float | None = None) -> CoolingStage:
    plant = p["plant"]
    total = float(required_cooling_mw(year, p, affected_fraction))
    source = float(source_temperature_c(year, p))
    dry_delta = max(source - dry_outlet_temperature_c(p), 0.0)
    dry = min(total, thermal_capacitance_mw_per_k(p, affected_fraction) * dry_delta) if source > dry_outlet_temperature_c(p) else 0.0
    chiller = total - dry
    condenser = chiller * (1.0 + 1.0 / plant["chiller_cop"])
    flow = p["water"]["discharge_m3_s"] * (p["scenario"]["affected_flow_fraction"] if affected_fraction is None else affected_fraction)
    pump_mw = 0.0
    if total > 0.0:
        pump_mw = p["water"]["density_kg_m3"] * plant["gravity_m_s2"] * flow * plant["pump_head_m"] / plant["pump_efficiency"] / 1e6
    fan_mw = plant["dry_auxiliary_fraction"] * (dry + condenser)
    electricity = chiller / plant["chiller_cop"] + fan_mw + pump_mw
    air_rejection = dry + condenser + fan_mw + pump_mw
    return CoolingStage(total, dry, chiller, electricity, condenser, air_rejection)


def storage_heating_power_mw(p: dict[str, Any]) -> float:
    s = p["scenario"]
    w = p["water"]
    energy_j = w["density_kg_m3"] * s["pool_volume_m3"] * w["specific_heat_j_kgk"] * (s["boiling_temperature_c"] - s["initial_temperature_c"])
    return energy_j / (s["forecast_years"] * SECONDS_PER_YEAR) / 1e6


def evaporation_kg_s(cooling_mw: float, p: dict[str, Any]) -> float:
    return cooling_mw * 1e6 / p["water"]["latent_heat_j_kg"]


def dilution_flow_m3_s(year: float, p: dict[str, Any]) -> float:
    s = p["scenario"]
    w = p["water"]
    source = float(source_temperature_c(year, p))
    if source <= s["target_temperature_c"]:
        return 0.0
    hot_flow = w["discharge_m3_s"] * s["affected_flow_fraction"]
    return hot_flow * (source - s["target_temperature_c"]) / (s["target_temperature_c"] - w["cold_dilution_temperature_c"])


def passive_area_m2(cooling_mw: float, p: dict[str, Any]) -> float:
    passive = p["passive"]
    return cooling_mw * 1e6 / (passive["heat_transfer_w_m2k"] * passive["driving_temperature_k"])


def variable_capex_eur(year: float, p: dict[str, Any], technology: str = "hybrid") -> dict[str, float]:
    c = p["cost"]
    stage = cooling_stage(year, p)
    reserve = 1.0 + p["plant"]["reserve_fraction"]
    fraction = p["scenario"]["affected_flow_fraction"]
    backup = c["backup_power_eur"] * fraction ** c["backup_scale_exponent"]
    if technology == "hybrid":
        return {
            "exchanger": stage.total_mw * 1000.0 * c["exchanger_eur_kw"] * reserve,
            "chiller": stage.chiller_mw * 1000.0 * c["chiller_eur_kw"] * reserve,
            "dry_cooler": (stage.dry_mw + stage.condenser_mw) * 1000.0 * c["dry_cooler_eur_kw"] * reserve,
            "backup_power": backup if stage.total_mw > 0.0 else 0.0,
        }
    if technology == "evaporative":
        return {
            "exchanger": stage.total_mw * 1000.0 * c["exchanger_eur_kw"] * reserve,
            "evaporative": stage.total_mw * 1000.0 * c["evaporative_eur_kw"] * reserve,
            "backup_power": backup * 0.3 if stage.total_mw > 0.0 else 0.0,
        }
    if technology == "dilution":
        flow = dilution_flow_m3_s(year, p)
        pump_mw = p["water"]["density_kg_m3"] * p["plant"]["gravity_m_s2"] * flow * 20.0 / p["plant"]["pump_efficiency"] / 1e6
        return {"pumps": pump_mw * 1000.0 * c["dilution_pump_eur_kw"] * reserve}
    raise ValueError(f"Unknown technology: {technology}")


def cumulative_capex_eur(year: float, p: dict[str, Any], technology: str = "hybrid") -> float:
    c = p["cost"]
    multiplier = 1.0 + c["engineering_contingency_fraction"]
    fraction = p["scenario"]["affected_flow_fraction"]
    fixed = c["fixed_civil_eur"] * fraction ** c["civil_scale_exponent"] + c["controls_eur"] * fraction ** c["controls_scale_exponent"]
    if year < 1.0:
        return fixed
    return fixed + multiplier * sum(variable_capex_eur(year, p, technology).values())


def annual_operation(year: int, p: dict[str, Any], technology: str = "hybrid") -> dict[str, float]:
    plant = p["plant"]
    stage = cooling_stage(float(year), p)
    if technology == "hybrid":
        electricity_mw = stage.electricity_mw
        water_m3 = 0.0
        hygiene_eur = 0.0
    elif technology == "evaporative":
        electricity_mw = plant["dry_auxiliary_fraction"] * stage.total_mw
        if stage.total_mw > 0.0:
            electricity_mw += p["water"]["density_kg_m3"] * plant["gravity_m_s2"] * p["water"]["discharge_m3_s"] * plant["pump_head_m"] / plant["pump_efficiency"] / 1e6
        water_m3 = evaporation_kg_s(stage.total_mw, p) / p["water"]["density_kg_m3"] * SECONDS_PER_YEAR
        hygiene_eur = p["cost"]["evaporative_hygiene_eur_year"] if stage.total_mw > 0.0 else 0.0
    elif technology == "dilution":
        flow = dilution_flow_m3_s(float(year), p)
        electricity_mw = p["water"]["density_kg_m3"] * plant["gravity_m_s2"] * flow * 20.0 / plant["pump_efficiency"] / 1e6
        water_m3 = flow * SECONDS_PER_YEAR
        hygiene_eur = 0.0
    else:
        raise ValueError(f"Unknown technology: {technology}")
    electricity_mwh = electricity_mw * HOURS_PER_YEAR
    energy_cost = electricity_mwh * plant["electricity_price_eur_mwh"]
    water_cost = water_m3 * p["cost"]["water_price_eur_m3"]
    heat_credit = plant["heat_recovery_mw"] * plant["heat_recovery_hours"] * plant["heat_value_eur_mwh"] if technology == "hybrid" and stage.total_mw >= plant["heat_recovery_mw"] else 0.0
    return {
        "electricity_mw": electricity_mw,
        "electricity_mwh": electricity_mwh,
        "energy_cost_eur": energy_cost,
        "water_m3": water_m3,
        "water_cost_eur": water_cost,
        "hygiene_eur": hygiene_eur,
        "heat_credit_eur": heat_credit,
    }


def economic_schedule(p: dict[str, Any], technology: str = "hybrid", upfront: bool = False) -> list[dict[str, float]]:
    horizon = int(p["scenario"]["horizon_years"])
    final_capex = cumulative_capex_eur(p["scenario"]["forecast_years"], p, technology)
    rows = []
    previous_capex = 0.0
    for year in range(horizon + 1):
        if upfront:
            installed = final_capex if year >= 0 else 0.0
            investment = final_capex if year == 0 else 0.0
        else:
            installed = cumulative_capex_eur(float(min(year, p["scenario"]["forecast_years"])), p, technology)
            investment = max(installed - previous_capex, 0.0)
        previous_capex = installed
        operation = annual_operation(year, p, technology)
        replacement = 0.0
        if year == p["plant"]["replacement_year"]:
            replacement = p["plant"]["replacement_fraction"] * sum(variable_capex_eur(p["scenario"]["forecast_years"], p, technology).values())
        maintenance = p["plant"]["maintenance_fraction"] * installed
        net_operation = operation["energy_cost_eur"] + operation["water_cost_eur"] + operation["hygiene_eur"] + maintenance - operation["heat_credit_eur"]
        total = investment + replacement + net_operation
        discount = (1.0 + p["plant"]["discount_rate"]) ** year
        rows.append({
            "year": float(year),
            "source_temperature_c": float(source_temperature_c(float(year), p)),
            "required_cooling_mw": float(required_cooling_mw(float(year), p)),
            "installed_capex_eur": installed,
            "investment_eur": investment,
            "replacement_eur": replacement,
            "maintenance_eur": maintenance,
            "net_operation_eur": net_operation,
            "total_cost_eur": total,
            "present_value_eur": total / discount,
            **operation,
        })
    return rows


def npv(rows: list[dict[str, float]]) -> float:
    return sum(row["present_value_eur"] for row in rows)
