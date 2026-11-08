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


@dataclass(frozen=True)
class AbsorptionStage:
    total_mw: float
    generator_mw: float
    evaporator_mw: float
    rejection_mw: float
    auxiliary_mw: float
    dry_cooling_mw: float
    chiller_mw: float
    secondary_hot_inlet_c: float
    secondary_return_c: float
    secondary_flow_m3_s: float
    source_after_generator_c: float
    source_after_evaporator_c: float


def heating_rate_k_per_year(p: dict[str, Any]) -> float:
    s = p["scenario"]
    return (s["boiling_temperature_c"] - s["initial_temperature_c"]) / s["forecast_years"]


def source_temperature_c(year: float | np.ndarray, p: dict[str, Any]) -> float | np.ndarray:
    s = p["scenario"]
    temperature = s["initial_temperature_c"] + heating_rate_k_per_year(p) * np.asarray(year)
    return np.minimum(temperature, s["source_temperature_cap_c"])


def planned_return_temperature_c(time_hours: float | np.ndarray, p: dict[str, Any]) -> np.ndarray:
    e = p["ecology"]
    temperature = e["ramp_stress_start_c"] - e["maximum_return_rate_k_h"] * np.asarray(time_hours)
    return np.maximum(temperature, p["scenario"]["target_temperature_c"])


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


def design_flow_ratio(p: dict[str, Any]) -> float:
    return p["hydrology"]["design_discharge_m3_s"] / p["water"]["discharge_m3_s"]


def design_electrical_stage(p: dict[str, Any], affected_fraction: float | None = None, technology: str = "hybrid") -> CoolingStage:
    design_p = dict(p, plant=dict(p["plant"], chiller_cop=p["uncertainty"]["cop_low"]))
    fraction = design_flow_ratio(p) * p["scenario"]["affected_flow_fraction"] if affected_fraction is None else affected_fraction
    return cooling_stage(p["scenario"]["forecast_years"], design_p, affected_fraction=fraction, technology=technology)


def absorption_stage(year: float, p: dict[str, Any], affected_fraction: float | None = None) -> AbsorptionStage:
    plant = p["plant"]
    total = float(required_cooling_mw(year, p, affected_fraction))
    source = float(source_temperature_c(year, p))
    capacitance = thermal_capacitance_mw_per_k(p, affected_fraction)
    hot_return = plant["absorption_generator_return_c"]
    approach = plant["absorption_approach_k"]
    source_after_generator = hot_return + approach
    secondary_hot_inlet = source - approach
    fraction = p["scenario"]["affected_flow_fraction"] if affected_fraction is None else affected_fraction
    source_flow = p["water"]["discharge_m3_s"] * fraction
    secondary_flow = plant["absorption_secondary_flow_m3_s"] * source_flow / p["water"]["discharge_m3_s"]
    if source < hot_return + 2.0 * approach:
        outlet = dry_outlet_temperature_c(p)
        dry = min(total, capacitance * max(source - outlet, 0.0)) if source > outlet else 0.0
        return AbsorptionStage(total, 0.0, 0.0, 0.0, 0.0, dry, total - dry, secondary_hot_inlet, hot_return, secondary_flow, source, source - dry / capacitance)
    generator = capacitance * (source - source_after_generator)
    evaporator = min(generator * plant["absorption_thermal_cop"], total - generator)
    source_after_evaporator = source_after_generator - evaporator / capacitance
    remaining = total - generator - evaporator
    outlet = dry_outlet_temperature_c(p)
    dry = min(remaining, capacitance * max(source_after_evaporator - outlet, 0.0)) if source_after_evaporator > outlet else 0.0
    return AbsorptionStage(
        total,
        generator,
        evaporator,
        generator + evaporator,
        evaporator * plant["absorption_auxiliary_fraction"],
        dry,
        remaining - dry,
        secondary_hot_inlet,
        hot_return,
        secondary_flow,
        source_after_generator,
        source_after_evaporator,
    )


def cooling_stage(year: float, p: dict[str, Any], affected_fraction: float | None = None, technology: str = "hybrid") -> CoolingStage:
    plant = p["plant"]
    total = float(required_cooling_mw(year, p, affected_fraction))
    source = float(source_temperature_c(year, p))
    absorption_auxiliary = 0.0
    if technology == "absorption":
        absorption = absorption_stage(year, p, affected_fraction)
        dry = absorption.generator_mw + absorption.evaporator_mw + absorption.dry_cooling_mw
        chiller = absorption.chiller_mw
        absorption_auxiliary = absorption.auxiliary_mw
    else:
        if technology == "hybrid":
            outlet = dry_outlet_temperature_c(p)
        elif technology == "evaporative":
            outlet = plant.get("evaporative_source_outlet_c", plant["wet_bulb_design_c"] + plant["evaporative_approach_k"])
        else:
            raise ValueError(f"Unknown cooling stage: {technology}")
        dry_delta = max(source - outlet, 0.0)
        dry = min(total, thermal_capacitance_mw_per_k(p, affected_fraction) * dry_delta) if source > outlet else 0.0
        chiller = total - dry
    condenser = chiller * (1.0 + 1.0 / plant["chiller_cop"])
    flow = p["water"]["discharge_m3_s"] * (p["scenario"]["affected_flow_fraction"] if affected_fraction is None else affected_fraction)
    pump_mw = 0.0
    if total > 0.0:
        pump_mw = p["water"]["density_kg_m3"] * plant["gravity_m_s2"] * flow * plant["pump_head_m"] / plant["pump_efficiency"] / 1e6
    fan_mw = plant["dry_auxiliary_fraction"] * (dry + condenser)
    electricity = chiller / plant["chiller_cop"] + fan_mw + pump_mw + absorption_auxiliary
    air_rejection = dry + condenser + fan_mw + pump_mw + absorption_auxiliary
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


def backup_fuel_liters(p: dict[str, Any], technology: str = "hybrid") -> float:
    plant = p["plant"]
    final_electricity_mw = design_electrical_stage(p, technology=technology).electricity_mw
    return final_electricity_mw * 1000.0 * plant["backup_duration_hours"] / (plant["backup_thermal_efficiency"] * plant["diesel_energy_kwh_l"])


def backup_fuel_cost_eur(p: dict[str, Any], technology: str = "hybrid") -> float:
    return backup_fuel_liters(p, technology) * p["plant"]["diesel_price_eur_l"]


def variable_capex_eur(year: float, p: dict[str, Any], technology: str = "hybrid") -> dict[str, float]:
    c = p["cost"]
    stage_technology = technology if technology in {"hybrid", "evaporative", "absorption"} else "hybrid"
    stage = cooling_stage(year, p, technology=stage_technology)
    capacity_scale = design_flow_ratio(p) * (1.0 + p["plant"]["reserve_fraction"])
    design_affected_fraction = design_flow_ratio(p) * p["scenario"]["affected_flow_fraction"]
    design_electricity_mw = design_electrical_stage(p, affected_fraction=design_affected_fraction, technology=stage_technology).electricity_mw
    reference_scenario = dict(p["scenario"], target_temperature_c=p["scenario"]["initial_temperature_c"], affected_flow_fraction=1.0)
    reference_p = dict(p, scenario=reference_scenario, hydrology=dict(p["hydrology"], design_discharge_m3_s=p["hydrology"]["discharge_p90_m3_s"]))
    reference_electricity_mw = design_electrical_stage(reference_p, technology=stage_technology).electricity_mw
    electricity_ratio = design_electricity_mw / reference_electricity_mw if reference_electricity_mw > 0.0 else 0.0
    backup = (c["backup_power_eur"] + backup_fuel_cost_eur(reference_p, stage_technology)) * electricity_ratio
    chiller_cost = c["chiller_eur_kw"] * c["legacy_escalation_factor"]
    dry_cooler_cost = c["dry_cooler_eur_kw"] * c["legacy_escalation_factor"]
    evaporative_cost = c["evaporative_eur_kw"] * c["legacy_escalation_factor"]
    if technology == "hybrid":
        return {
            "exchanger": stage.total_mw * 1000.0 * c["exchanger_eur_kw"] * capacity_scale,
            "chiller": stage.chiller_mw * 1000.0 * chiller_cost * capacity_scale,
            "dry_cooler": (stage.dry_mw + stage.condenser_mw) * 1000.0 * dry_cooler_cost * capacity_scale,
            "backup_power": backup if stage.total_mw > 0.0 else 0.0,
        }
    if technology == "evaporative":
        return {
            "exchanger": stage.total_mw * 1000.0 * c["exchanger_eur_kw"] * capacity_scale,
            "evaporative": stage.dry_mw * 1000.0 * evaporative_cost * capacity_scale,
            "chiller": stage.chiller_mw * 1000.0 * chiller_cost * capacity_scale,
            "dry_cooler": stage.condenser_mw * 1000.0 * dry_cooler_cost * capacity_scale,
            "backup_power": backup if stage.total_mw > 0.0 else 0.0,
        }
    if technology == "absorption":
        absorption = absorption_stage(year, p)
        return {
            "exchanger": stage.total_mw * 1000.0 * c["exchanger_eur_kw"] * capacity_scale,
            "absorption_chiller": absorption.evaporator_mw * 1000.0 * c["absorption_eur_kw"] * c["legacy_escalation_factor"] * capacity_scale,
            "chiller": stage.chiller_mw * 1000.0 * chiller_cost * capacity_scale,
            "dry_cooler": (stage.dry_mw + stage.condenser_mw) * 1000.0 * dry_cooler_cost * capacity_scale,
            "backup_power": backup if stage.total_mw > 0.0 else 0.0,
        }
    if technology == "dilution":
        flow = dilution_flow_m3_s(year, p)
        pump_mw = p["water"]["density_kg_m3"] * p["plant"]["gravity_m_s2"] * flow * 20.0 / p["plant"]["pump_efficiency"] / 1e6
        return {"pumps": pump_mw * 1000.0 * c["dilution_pump_eur_kw"] * capacity_scale}
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
    stage = cooling_stage(float(year), p, technology=technology if technology in {"hybrid", "evaporative", "absorption"} else "hybrid")
    if technology in {"hybrid", "absorption"}:
        electricity_mw = stage.electricity_mw
        water_m3 = 0.0
        hygiene_eur = 0.0
    elif technology == "evaporative":
        electricity_mw = stage.electricity_mw
        water_m3 = evaporation_kg_s(stage.dry_mw, p) / p["water"]["density_kg_m3"] * SECONDS_PER_YEAR
        hygiene_eur = p["cost"]["evaporative_hygiene_eur_year"] if stage.total_mw > 0.0 else 0.0
    elif technology == "dilution":
        flow = dilution_flow_m3_s(float(year), p)
        electricity_mw = p["water"]["density_kg_m3"] * plant["gravity_m_s2"] * flow * 20.0 / plant["pump_efficiency"] / 1e6
        water_m3 = flow * SECONDS_PER_YEAR
        hygiene_eur = 0.0
    else:
        raise ValueError(f"Unknown technology: {technology}")
    electricity_mwh = electricity_mw * HOURS_PER_YEAR * plant["availability"]
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


def economic_schedule(p: dict[str, Any], technology: str = "hybrid", upfront: bool = False, backup_shortfall: bool = False) -> list[dict[str, float]]:
    if backup_shortfall and technology != "hybrid":
        raise ValueError("Backup shortfall is only defined for the hybrid technology")
    plant = p["plant"]
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
        if year == 0:
            operation = {key: 0.0 for key in operation}
        replacement = 0.0
        if year == plant["replacement_year"]:
            replacement = plant["replacement_fraction"] * (1.0 + p["cost"]["engineering_contingency_fraction"]) * sum(variable_capex_eur(p["scenario"]["forecast_years"], p, technology).values())
        maintenance = plant["maintenance_fraction"] * installed if year > 0 else 0.0
        backup_mwh = operation["electricity_mw"] * HOURS_PER_YEAR * (1.0 - plant["availability"]) if backup_shortfall and year > 0 else 0.0
        backup_liters = backup_mwh * 1000.0 / (plant["backup_thermal_efficiency"] * plant["diesel_energy_kwh_l"])
        backup_cost = backup_liters * plant["diesel_price_eur_l"]
        net_operation = operation["energy_cost_eur"] + operation["water_cost_eur"] + operation["hygiene_eur"] + maintenance - operation["heat_credit_eur"] + backup_cost
        total = investment + replacement + net_operation
        discount = (1.0 + plant["discount_rate"]) ** year
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
            "backup_electricity_mwh": backup_mwh,
            "backup_fuel_liters": backup_liters,
            "backup_cost_eur": backup_cost,
            **operation,
        })
    return rows


def npv(rows: list[dict[str, float]]) -> float:
    return sum(row["present_value_eur"] for row in rows)
