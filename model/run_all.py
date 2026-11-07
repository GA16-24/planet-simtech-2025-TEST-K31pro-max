from __future__ import annotations

import copy
import csv
import hashlib
import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import yaml

from core import (
    HOURS_PER_YEAR,
    backup_fuel_liters,
    cooling_stage,
    cumulative_capex_eur,
    dilution_flow_m3_s,
    economic_schedule,
    evaporation_kg_s,
    heating_rate_k_per_year,
    npv,
    passive_area_m2,
    planned_return_temperature_c,
    required_cooling_mw,
    source_temperature_c,
    storage_heating_power_mw,
    thermal_capacitance_mw_per_k,
    variable_capex_eur,
)
from validation import run_validation

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "model"
FIG = ROOT / "report" / "figures"
GEN = ROOT / "report" / "generated"
for directory in (OUT, FIG, GEN):
    directory.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 14,
    "axes.titlesize": 16,
    "axes.labelsize": 14,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 160,
    "savefig.bbox": "tight",
    "pdf.fonttype": 42,
})
BLUE = "#176B87"
ORANGE = "#D97732"
GREEN = "#3D7A57"
RED = "#A84343"
GRAY = "#64707A"


def save_figure(fig: plt.Figure, name: str) -> None:
    fig.savefig(FIG / f"{name}.png", dpi=220)
    fig.savefig(FIG / f"{name}.pdf", metadata={"Creator": "model/run_all.py", "CreationDate": None})
    plt.close(fig)


def macro(name: str, value: float, digits: int = 2) -> str:
    return f"\\newcommand{{\\{name}}}{{{value:.{digits}f}}}\n".replace(".", ",")


def jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(item) for item in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.floating, np.integer)):
        return value.item()
    return value


def alternative_result(p: dict[str, Any], technology: str, name: str, verdict: str) -> dict[str, Any]:
    rows = economic_schedule(p, technology)
    final = rows[int(p["scenario"]["forecast_years"])]
    return {
        "id": technology,
        "name": name,
        "verdict": verdict,
        "final_capex_eur": final["installed_capex_eur"],
        "annual_electricity_mwh": final["electricity_mwh"],
        "emissions_tco2_year": final["electricity_mwh"] * p["emissions"]["carbon_intensity_tco2_mwh"],
        "annual_water_m3": final["water_m3"],
        "annual_operating_eur": final["net_operation_eur"],
        "npv_25y_eur": npv(rows),
        "schedule": rows,
    }


def coupled_npv(p: dict[str, Any], discharge: float, cop: float, capex_multiplier: float) -> float:
    plant = p["plant"]
    cost = p["cost"]
    flow_ratio = discharge / p["water"]["discharge_m3_s"]
    final_stage = cooling_stage(p["scenario"]["forecast_years"], p)
    final_dry = final_stage.dry_mw * flow_ratio
    final_chiller = final_stage.chiller_mw * flow_ratio
    final_condenser = final_chiller * (1.0 + 1.0 / cop)
    final_pump = p["water"]["density_kg_m3"] * plant["gravity_m_s2"] * discharge * plant["pump_head_m"] / plant["pump_efficiency"] / 1e6
    final_electricity = final_chiller / cop + plant["dry_auxiliary_fraction"] * (final_dry + final_condenser) + final_pump
    rows = []
    previous_installed = 0.0
    final_variable = 0.0
    for year in range(int(p["scenario"]["horizon_years"]) + 1):
        stage = cooling_stage(float(min(year, p["scenario"]["forecast_years"])), p)
        dry = stage.dry_mw * flow_ratio
        chiller = stage.chiller_mw * flow_ratio
        condenser = chiller * (1.0 + 1.0 / cop)
        total = stage.total_mw * flow_ratio
        pump = 0.0
        if total > 0.0:
            pump = p["water"]["density_kg_m3"] * plant["gravity_m_s2"] * discharge * plant["pump_head_m"] / plant["pump_efficiency"] / 1e6
        fan = plant["dry_auxiliary_fraction"] * (dry + condenser)
        electricity = chiller / cop + fan + pump
        energy_cost = electricity * HOURS_PER_YEAR * plant["availability"] * plant["electricity_price_eur_mwh"]
        parts = variable_capex_eur(float(min(year, p["scenario"]["forecast_years"])), p)
        backup_ratio = final_electricity / cooling_stage(p["scenario"]["forecast_years"], p).electricity_mw if cooling_stage(p["scenario"]["forecast_years"], p).electricity_mw > 0.0 else 0.0
        variable = (
            parts["exchanger"] * flow_ratio
            + parts["chiller"] * flow_ratio
            + (dry + condenser) * 1000.0 * cost["dry_cooler_eur_kw"] * (1.0 + plant["reserve_fraction"])
            + parts["backup_power"] * backup_ratio
        )
        fixed = (
            cost["fixed_civil_eur"] * flow_ratio ** cost["civil_scale_exponent"]
            + cost["controls_eur"] * flow_ratio ** cost["controls_scale_exponent"]
        )
        installed = capex_multiplier * (fixed + (1.0 + cost["engineering_contingency_fraction"]) * variable)
        investment = max(installed - previous_installed, 0.0)
        previous_installed = installed
        if year == plant["replacement_year"]:
            final_variable = variable
        replacement = 0.0
        if year == plant["replacement_year"]:
            replacement = plant["replacement_fraction"] * capex_multiplier * (1.0 + cost["engineering_contingency_fraction"]) * final_variable
        maintenance = plant["maintenance_fraction"] * installed
        total_cost = investment + replacement + maintenance + energy_cost
        rows.append(total_cost / (1.0 + plant["discount_rate"]) ** year)
    return float(sum(rows))


def main() -> None:
    with (ROOT / "data" / "parameters.yml").open(encoding="utf-8") as handle:
        p = yaml.safe_load(handle)
    s = p["scenario"]
    final_year = int(s["forecast_years"])
    final_q = float(required_cooling_mw(final_year, p))
    final_stage = cooling_stage(final_year, p)
    validation = run_validation(p)
    baseline_coupled_npv = coupled_npv(p, p["water"]["discharge_m3_s"], p["plant"]["chiller_cop"], 1.0)
    validation["coupled_npv_error_eur"] = abs(baseline_coupled_npv - npv(economic_schedule(p, "hybrid")))
    assert validation["coupled_npv_error_eur"] < 1e-6

    alternatives = [
        alternative_result(p, "hybrid", "H1 Zweistufige Vollstromkühlung", "Referenz, dauerhaft innerhalb der Auslegungshülle"),
        alternative_result(p, "evaporative", "H2 Geschlossene Verdunstungskühlung", "Physikalisch wirksam, aber Wasserverlust und Hygieneregeln"),
        alternative_result(p, "dilution", "H3 Kaltwasserzumischung", "Keine ausreichende Kaltwasserquelle belegt"),
    ]
    hybrid_staged = economic_schedule(p, "hybrid", upfront=False)
    hybrid_upfront = economic_schedule(p, "hybrid", upfront=True)
    evaporation = evaporation_kg_s(final_q, p)
    dilution = dilution_flow_m3_s(final_year, p)
    passive_area = passive_area_m2(final_q, p)
    storage_mw = storage_heating_power_mw(p)

    sensitivity_specs = [
        ("Abfluss 0,7 m³/s", "water.discharge_m3_s", p["hydrology"]["discharge_p10_m3_s"]),
        ("Abfluss 4,7 m³/s", "water.discharge_m3_s", p["hydrology"]["discharge_p90_m3_s"]),
        ("Sieden nach 8 Jahren", "scenario.forecast_years", 8.0),
        ("Sieden nach 12 Jahren", "scenario.forecast_years", 12.0),
        ("Ziel 7 °C", "scenario.target_temperature_c", 7.0),
        ("Ziel 11 °C", "scenario.target_temperature_c", 11.0),
    ]
    sensitivity = []
    for label, path, value in sensitivity_specs:
        varied = copy.deepcopy(p)
        section, key = path.split(".")
        varied[section][key] = value
        q = float(required_cooling_mw(varied["scenario"]["forecast_years"], varied))
        varied_npv = npv(economic_schedule(varied, "hybrid"))
        sensitivity.append({"case": label, "value": value, "final_cooling_mw": q, "relative_change": q / final_q - 1.0, "npv_25y_eur": varied_npv})

    flow_fraction_scenarios = []
    for fraction in [1.0, 0.1, 0.01, 0.001]:
        varied = copy.deepcopy(p)
        varied["scenario"]["affected_flow_fraction"] = fraction
        rows = economic_schedule(varied, "hybrid")
        stage = cooling_stage(final_year, varied)
        flow_fraction_scenarios.append({
            "affected_fraction": fraction,
            "final_cooling_mw": stage.total_mw,
            "electricity_mw": stage.electricity_mw,
            "final_capex_eur": rows[final_year]["installed_capex_eur"],
            "annual_operating_eur": rows[final_year]["net_operation_eur"],
            "npv_25y_eur": npv(rows),
        })

    rng = np.random.default_rng(p["uncertainty"]["random_seed"])
    count = int(p["uncertainty"]["sample_count"])
    discharge_samples = rng.triangular(
        p["uncertainty"]["discharge_low_m3_s"],
        p["uncertainty"]["discharge_mode_m3_s"],
        p["uncertainty"]["discharge_high_m3_s"],
        count,
    )
    q_samples = thermal_capacitance_mw_per_k(p) * discharge_samples / p["water"]["discharge_m3_s"] * (s["boiling_temperature_c"] - s["target_temperature_c"])
    cop_samples = rng.triangular(p["uncertainty"]["cop_low"], p["uncertainty"]["cop_mode"], p["uncertainty"]["cop_high"], count)
    capex_samples = rng.lognormal(mean=-0.5 * p["uncertainty"]["capex_multiplier_sigma"] ** 2, sigma=p["uncertainty"]["capex_multiplier_sigma"], size=count)
    npv_samples = np.array([
        coupled_npv(p, float(discharge), float(cop), float(capex))
        for discharge, cop, capex in zip(discharge_samples, cop_samples, capex_samples)
    ])

    availability_scenarios = []
    for availability in [0.95, 0.98, 1.0]:
        varied = copy.deepcopy(p)
        varied["plant"]["availability"] = availability
        rows = economic_schedule(varied, "hybrid")
        availability_scenarios.append({"availability": availability, "npv_25y_eur": npv(rows), "final_electricity_mwh": rows[final_year]["electricity_mwh"]})

    weather_scenarios = []
    for air_temperature in [30.0, 35.0, 38.0]:
        varied = copy.deepcopy(p)
        varied["plant"]["summer_design_air_c"] = air_temperature
        rows = economic_schedule(varied, "hybrid")
        stage = cooling_stage(final_year, varied)
        weather_scenarios.append({"summer_air_c": air_temperature, "electricity_mw": stage.electricity_mw, "npv_25y_eur": npv(rows)})

    years = np.linspace(0.0, 12.0, 481)
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.5))
    axes[0].plot(years, source_temperature_c(years, p), color=BLUE, lw=2)
    axes[0].axhline(s["target_temperature_c"], color=GREEN, ls="--", lw=1, label="Regelziel 9 °C")
    axes[0].axvline(10, color=GRAY, lw=0.8)
    axes[0].set(xlabel="Jahre seit Prognosebeginn", ylabel="Tiefentemperatur in °C", title="Szenarioannahme")
    axes[0].legend(frameon=False, loc="upper left")
    for fraction, color, label in [(1.0, BLUE, "Gesamter Quellstrom"), (0.01, ORANGE, "1 % des Quellstroms"), (0.001, GREEN, "0,1 % des Quellstroms")]:
        axes[1].plot(years, required_cooling_mw(years, p, fraction), color=color, lw=2, label=label)
    axes[1].set(xlabel="Jahre seit Prognosebeginn", ylabel="Kühlleistung in MW", title="Erforderliche Wärmeabfuhr")
    axes[1].set_yscale("symlog", linthresh=1.0)
    fig.legend(handles=axes[1].get_lines(), frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(0.5, 0.005))
    fig.subplots_adjust(bottom=0.38, wspace=0.35)
    save_figure(fig, "fig01_prognose_last")

    schedule_years = np.arange(0, 13)
    stages = [cooling_stage(float(year), p) for year in schedule_years]
    fig, ax = plt.subplots(figsize=(8.6, 3.8))
    ax.stackplot(schedule_years, [stage.dry_mw for stage in stages], [stage.chiller_mw for stage in stages], labels=["Trockenkühlung", "Kältemaschinen"], colors=[BLUE, ORANGE], alpha=0.9)
    ax.plot(schedule_years, [stage.total_mw * 1.2 for stage in stages], color=RED, lw=1.8, ls="--", label="Auslegung mit 20 % Reserve")
    ax.set(xlabel="Jahre seit Prognosebeginn", ylabel="Leistung in MW", title="Modularer Ausbau der Vollstromkühlung")
    ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.24))
    fig.subplots_adjust(bottom=0.34)
    save_figure(fig, "fig02_stufenplan")

    fig, ax = plt.subplots(figsize=(8.6, 3.8))
    for technology, color, label in [("hybrid", BLUE, "H1 Hybrid"), ("evaporative", ORANGE, "H2 Verdunstung")]:
        rows = economic_schedule(p, technology)
        cumulative = np.cumsum([row["present_value_eur"] for row in rows]) / 1e9
        ax.plot([row["year"] for row in rows], cumulative, color=color, lw=2, label=label)
    ax.set(xlabel="Betriebsjahr", ylabel="Kumulierte Barwertkosten in Mrd. €", title="Kostenpfad über 25 Jahre")
    ax.legend(frameon=False, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.24))
    fig.subplots_adjust(bottom=0.32)
    save_figure(fig, "fig03_kostenpfad")

    fig, ax = plt.subplots(figsize=(8.6, 3.8))
    labels = [row["case"] for row in sensitivity]
    values = [row["final_cooling_mw"] for row in sensitivity]
    positions = np.arange(len(labels))
    ax.barh(positions, values, color=[BLUE if value <= final_q else ORANGE for value in values])
    ax.axvline(final_q, color=RED, ls="--", lw=1.4, label=f"Referenz {final_q:.1f} MW")
    ax.set_yticks(positions, labels)
    ax.invert_yaxis()
    ax.set(xlabel="Kühlleistung im Prognosejahr in MW", title="Deterministische Sensitivität")
    ax.legend(frameon=False, loc="lower right")
    save_figure(fig, "fig04_sensitivitaet")

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.5))
    axes[0].hist(q_samples, bins=45, color=BLUE, alpha=0.85)
    axes[0].axvline(final_q, color=RED, ls="--", lw=1.4)
    axes[0].set(xlabel="Kühlleistung in MW", ylabel="Anzahl", title="Abflussunsicherheit")
    axes[1].hist(npv_samples / 1e9, bins=45, color=ORANGE, alpha=0.85)
    axes[1].axvline(npv(hybrid_staged) / 1e9, color=RED, ls="--", lw=1.4)
    axes[1].set(xlabel="Barwertkosten in Mrd. €", ylabel="Anzahl", title="COP und Investitionskosten")
    fig.tight_layout()
    save_figure(fig, "fig05_unsicherheit")

    fractions = np.logspace(-4, 0, 200)
    fig, ax = plt.subplots(figsize=(8.6, 3.8))
    ax.loglog(fractions * 100.0, final_q * fractions, color=BLUE, lw=2)
    ax.axhline(storage_mw, color=GREEN, ls="--", label=f"Speichergrenze {storage_mw:.3f} MW")
    ax.axvline(1.0, color=ORANGE, ls=":", label="1 %-Teilstrom")
    ax.set(xlabel="Erfasster Anteil des Quellstroms in %", ylabel="Kühlleistung in MW", title="Maßstab der Anlage hängt vom erfassten Strom ab")
    ax.legend(frameon=False)
    save_figure(fig, "fig06_teilstrom")

    results = {
        "model_version": "1.1.0",
        "parameters": p,
        "baseline": {
            "heating_rate_k_year": heating_rate_k_per_year(p),
            "thermal_capacitance_mw_k": thermal_capacitance_mw_per_k(p),
            "final_cooling_mw": final_q,
            "dry_cooling_mw": final_stage.dry_mw,
            "chiller_mw": final_stage.chiller_mw,
            "electricity_mw": final_stage.electricity_mw,
            "electricity_mwh_year": final_stage.electricity_mw * HOURS_PER_YEAR * p["plant"]["availability"],
            "condenser_heat_mw": final_stage.condenser_mw,
            "air_rejection_mw": final_stage.air_rejection_mw,
            "air_face_area_m2": final_stage.air_rejection_mw * 1e6 / (p["air"]["face_velocity_m_s"] * p["air"]["density_kg_m3"] * p["air"]["specific_heat_j_kgk"] * p["air"]["temperature_rise_k"]),
            "air_service_area_m2": final_stage.air_rejection_mw * 1e6 / (p["air"]["face_velocity_m_s"] * p["air"]["density_kg_m3"] * p["air"]["specific_heat_j_kgk"] * p["air"]["temperature_rise_k"]) * p["air"]["service_area_factor"],
            "emissions_tco2_year": final_stage.electricity_mw * HOURS_PER_YEAR * p["plant"]["availability"] * p["emissions"]["carbon_intensity_tco2_mwh"],
            "backup_fuel_liters": backup_fuel_liters(p),
            "return_ramp_hours": (p["scenario"]["source_temperature_cap_c"] - p["scenario"]["target_temperature_c"]) / p["ecology"]["maximum_return_rate_k_h"],
            "return_ramp_max_rate_k_h": validation["return_ramp_max_rate_k_h"],
            "npsh_design_margin_bar": p["plant"]["intake_design_pressure_bar"] - 1.01325,
            "npsh_design_margin_m": (p["plant"]["intake_design_pressure_bar"] - 1.01325) * 1e5 / (p["water"]["density_kg_m3"] * p["plant"]["gravity_m_s2"]),
            "flood_stress_cooling_mw": float(required_cooling_mw(final_year, p) * p["hydrology"]["discharge_flood_m3_s"] / p["water"]["discharge_m3_s"]),
            "return_buffer_m3": p["water"]["discharge_m3_s"] * p["ecology"]["return_buffer_hours"] * 3600.0,
            "module_pipe_diameter_m": float(np.sqrt(4.0 * p["water"]["discharge_m3_s"] / p["plant"]["required_modules"] / (np.pi * p["plant"]["module_design_velocity_m_s"]))),
            "reserve_installed_mw": final_q * (1 + p["plant"]["reserve_fraction"]),
            "per_module_required_mw": final_q / p["plant"]["required_modules"],
            "storage_lower_bound_mw": storage_mw,
            "evaporation_kg_s": evaporation,
            "evaporation_m3_year": evaporation / p["water"]["density_kg_m3"] * 365 * 24 * 3600,
            "evaporation_flow_fraction": evaporation / p["water"]["density_kg_m3"] / p["water"]["discharge_m3_s"],
            "dilution_flow_m3_s": dilution,
            "dilution_to_natural_flow_ratio": dilution / p["water"]["discharge_m3_s"],
            "passive_area_m2": passive_area,
            "passive_area_km2": passive_area / 1e6,
            "hybrid_staged_npv_eur": npv(hybrid_staged),
            "hybrid_upfront_npv_eur": npv(hybrid_upfront),
            "staging_saving_eur": npv(hybrid_upfront) - npv(hybrid_staged),
            "final_capex_eur": cumulative_capex_eur(final_year, p, "hybrid"),
            "final_annual_operating_eur": hybrid_staged[final_year]["net_operation_eur"],
        },
        "alternatives": alternatives,
        "flow_fraction_scenarios": flow_fraction_scenarios,
        "availability_scenarios": availability_scenarios,
        "weather_scenarios": weather_scenarios,
        "sensitivity": sensitivity,
        "uncertainty": {
            "sample_count": count,
            "cooling_p05_mw": float(np.quantile(q_samples, 0.05)),
            "cooling_p50_mw": float(np.quantile(q_samples, 0.50)),
            "cooling_p95_mw": float(np.quantile(q_samples, 0.95)),
            "npv_p05_eur": float(np.quantile(npv_samples, 0.05)),
            "npv_p50_eur": float(np.quantile(npv_samples, 0.50)),
            "npv_p95_eur": float(np.quantile(npv_samples, 0.95)),
        },
        "validation": validation,
        "hybrid_schedule": hybrid_staged,
    }
    with (OUT / "results.json").open("w", encoding="utf-8") as handle:
        json.dump(jsonable(results), handle, ensure_ascii=False, indent=2)

    with (OUT / "hybrid_schedule.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, lineterminator="\n", fieldnames=list(hybrid_staged[0].keys()))
        writer.writeheader()
        writer.writerows(hybrid_staged)
    with (OUT / "sensitivity.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, lineterminator="\n", fieldnames=list(sensitivity[0].keys()))
        writer.writeheader()
        writer.writerows(sensitivity)
    np.savez(OUT / "uncertainty_samples.npz", cooling_mw=q_samples, npv_eur=npv_samples)

    macros = {
        "QFinal": (final_q, 1),
        "QFinalFull": (final_q, 3),
        "KDurchfluss": (thermal_capacitance_mw_per_k(p), 3),
        "QDry": (final_stage.dry_mw, 1),
        "QChiller": (final_stage.chiller_mw, 1),
        "PElectric": (final_stage.electricity_mw, 1),
        "EElectric": (final_stage.electricity_mw * HOURS_PER_YEAR / 1000, 1),
        "PChiller": (final_stage.chiller_mw / p["plant"]["chiller_cop"], 3),
        "PFans": (p["plant"]["dry_auxiliary_fraction"] * (final_stage.dry_mw + final_stage.condenser_mw), 3),
        "PPumps": (final_stage.electricity_mw - final_stage.chiller_mw / p["plant"]["chiller_cop"] - p["plant"]["dry_auxiliary_fraction"] * (final_stage.dry_mw + final_stage.condenser_mw), 3),
        "EnergyCostFinal": (hybrid_staged[final_year]["energy_cost_eur"] / 1e6, 2),
        "MaintenanceFinal": (hybrid_staged[final_year]["maintenance_eur"] / 1e6, 2),
        "QCondenser": (final_stage.condenser_mw, 1),
        "QAirRejection": (final_stage.air_rejection_mw, 1),
        "AirFaceArea": (results["baseline"]["air_face_area_m2"], 0),
        "AirServiceArea": (results["baseline"]["air_service_area_m2"] / 10000, 2),
        "EmissionsHybrid": (results["baseline"]["emissions_tco2_year"] / 1000, 1),
        "EmissionsEvap": (alternatives[1]["emissions_tco2_year"] / 1000, 1),
        "EmissionsDelta": ((results["baseline"]["emissions_tco2_year"] - alternatives[1]["emissions_tco2_year"]) / 1000, 1),
        "FuelReserve": (results["baseline"]["backup_fuel_liters"] / 1e6, 3),
        "ReturnRampHours": (results["baseline"]["return_ramp_hours"], 0),
        "ReturnRampRate": (results["baseline"]["return_ramp_max_rate_k_h"], 1),
        "NpshMargin": (results["baseline"]["npsh_design_margin_m"], 1),
        "AvailabilityLowNpv": (availability_scenarios[0]["npv_25y_eur"] / 1e9, 2),
        "AvailabilityHighNpv": (availability_scenarios[-1]["npv_25y_eur"] / 1e9, 2),
        "WeatherHighNpv": (weather_scenarios[-1]["npv_25y_eur"] / 1e9, 2),
        "QFloodStress": (results["baseline"]["flood_stress_cooling_mw"] / 1000, 2),
        "BufferVolume": (results["baseline"]["return_buffer_m3"], 0),
        "PipeDiameter": (results["baseline"]["module_pipe_diameter_m"], 2),
        "QReserve": (final_q * 1.2, 1),
        "QModule": (final_q / 5, 1),
        "QStorage": (storage_mw, 4),
        "EvapRate": (evaporation, 1),
        "EvapAnnual": (evaporation / p["water"]["density_kg_m3"] * 365 * 24 * 3600 / 1e6, 2),
        "EvapFraction": (100 * evaporation / p["water"]["density_kg_m3"] / p["water"]["discharge_m3_s"], 1),
        "DilutionFlow": (dilution, 1),
        "DilutionRatio": (dilution / p["water"]["discharge_m3_s"], 1),
        "PassiveArea": (passive_area / 1e6, 1),
        "CapexFinal": (cumulative_capex_eur(final_year, p, "hybrid") / 1e6, 0),
        "OpexFinal": (hybrid_staged[final_year]["net_operation_eur"] / 1e6, 1),
        "NpvHybrid": (npv(hybrid_staged) / 1e9, 2),
        "NpvUpfront": (npv(hybrid_upfront) / 1e9, 2),
        "NpvSaving": ((npv(hybrid_upfront) - npv(hybrid_staged)) / 1e6, 0),
        "NpvEvap": (alternatives[1]["npv_25y_eur"] / 1e9, 2),
        "NpvDilution": (alternatives[2]["npv_25y_eur"] / 1e9, 2),
        "FailureMinutes": (validation["failure_time_to_20c_h"] * 60, 0),
        "PoolTau": (validation["pool_time_constant_h"], 2),
        "QSampleLow": (results["uncertainty"]["cooling_p05_mw"], 0),
        "QSampleHigh": (results["uncertainty"]["cooling_p95_mw"], 0),
        "NpvSampleLow": (results["uncertainty"]["npv_p05_eur"] / 1e9, 2),
        "NpvSampleHigh": (results["uncertainty"]["npv_p95_eur"] / 1e9, 2),
    }
    with (GEN / "numbers.tex").open("w", encoding="utf-8") as handle:
        for name, (value, digits) in macros.items():
            handle.write(macro(name, value, digits))

    with (GEN / "alternatives.tex").open("w", encoding="utf-8") as handle:
        handle.write("\\begin{tabular}{@{}p{51mm}rrr@{}}\n\\toprule\nGröße im Auslegungsjahr & H1 Hybrid & H2 Verdunstung & H3 Zumischung \\\\\n\\midrule\n")
        rows = [
            ("Wärmeabfuhr in MW", "required_cooling_mw", 1.0, 1),
            ("Investition in Mio. €", "installed_capex_eur", 1e6, 1),
            ("Elektrische Leistung in MW", "electricity_mw", 1.0, 1),
            ("Strom pro Jahr in GWh", "electricity_mwh", 1000.0, 1),
            ("Betriebskosten in Mio. €", "net_operation_eur", 1e6, 1),
        ]
        for label, key, scale, digits in rows:
            values = [f"{alt['schedule'][final_year][key] / scale:.{digits}f}".replace(".", ",") for alt in alternatives]
            handle.write(f"{label} & {' & '.join(values)} \\\\\n")
        handle.write("Zusatzwasser pro Jahr & 0 m³ & ")
        handle.write(f"{alternatives[1]['annual_water_m3']/1e6:.2f}".replace(".", ",") + " Mio. m³ & " + f"{alternatives[2]['annual_water_m3']/1e9:.3f}".replace(".", ",") + " Mrd. m³ \\\\\n")
        npv_values = [f"{alt['npv_25y_eur']/1e9:.3f}".replace(".", ",") for alt in alternatives]
        handle.write("Barwert in Mrd. € & " + " & ".join(npv_values) + " \\\\\n")
        handle.write("\\bottomrule\n\\end{tabular}\n")

    with (GEN / "sensitivity.tex").open("w", encoding="utf-8") as handle:
        handle.write("\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nFall & Kühlleistung & Änderung & Barwert \\\\\n & in MW & in \\% & in Mrd. € \\\\\n\\midrule\n")
        for row in sensitivity:
            handle.write(f"{row['case']} & {row['final_cooling_mw']:.1f} & {100*row['relative_change']:+.1f} & {row['npv_25y_eur']/1e9:.3f} \\\\\n".replace(".", ","))
        handle.write("\\bottomrule\n\\end{tabular}\n")

    with (GEN / "flow_fractions.tex").open("w", encoding="utf-8") as handle:
        handle.write("\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nAnteil & Kühlung & Elektrik & Investition & Barwert \\\\\n & in MW & in MW & in Mio. € & in Mrd. € \\\\\n\\midrule\n")
        for row in flow_fraction_scenarios:
            handle.write(f"{100*row['affected_fraction']:.0f} \\% & {row['final_cooling_mw']:.1f} & {row['electricity_mw']:.2f} & {row['final_capex_eur']/1e6:.0f} & {row['npv_25y_eur']/1e9:.4f} \\\\\n".replace(".", ","))
        handle.write("\\bottomrule\n\\end{tabular}\n")

    manifest = {}
    for path in [ROOT / "data" / "parameters.yml", *sorted((ROOT / "model").glob("*.py")), OUT / "results.json", *sorted(FIG.glob("fig*.pdf"))]:
        manifest[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    with (OUT / "manifest.json").open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)

    print(f"Final cooling: {final_q:.3f} MW")
    print(f"Dry / chiller: {final_stage.dry_mw:.3f} / {final_stage.chiller_mw:.3f} MW")
    print(f"Electricity: {final_stage.electricity_mw:.3f} MW")
    print(f"Staged NPV: {npv(hybrid_staged)/1e9:.3f} billion EUR")
    print(f"Validation: {validation}")


if __name__ == "__main__":
    main()
