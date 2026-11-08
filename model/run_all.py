from __future__ import annotations

import copy
import csv
import hashlib
import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import yaml

from core import (
    HOURS_PER_YEAR,
    absorption_stage,
    backup_fuel_liters,
    cooling_stage,
    cumulative_capex_eur,
    dilution_flow_m3_s,
    design_flow_ratio,
    design_electrical_stage,
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
from validation import run_validation, simulate_failure

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "model"
FIG = ROOT / "report" / "figures"
GEN = ROOT / "report" / "generated"
for directory in (OUT, FIG, GEN):
    directory.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 18,
    "axes.titlesize": 18,
    "axes.labelsize": 18,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
    "legend.fontsize": 18,
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
    return f"\\newcommand{{\\{name}}}{{{value:.{digits}f}}}\n".replace(".", "{,}")


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
        "external_air_rejection_mw": 0.0 if technology == "dilution" else cooling_stage(p["scenario"]["forecast_years"], p, technology=technology).air_rejection_mw,
        "npv_25y_eur": npv(rows),
        "schedule": rows,
    }


def electrical_values_mw(p: dict[str, Any], discharge: float, cop: float, technology: str = "hybrid") -> tuple[float, float]:
    plant = p["plant"]
    flow_ratio = discharge / p["water"]["discharge_m3_s"]
    final_stage = cooling_stage(p["scenario"]["forecast_years"], p, technology=technology)
    dry = final_stage.dry_mw * flow_ratio
    chiller = final_stage.chiller_mw * flow_ratio
    condenser = chiller * (1.0 + 1.0 / cop)
    pump = p["water"]["density_kg_m3"] * plant["gravity_m_s2"] * discharge * plant["pump_head_m"] / plant["pump_efficiency"] / 1e6 if final_stage.total_mw > 0.0 else 0.0
    fan = plant["dry_auxiliary_fraction"] * (dry + condenser)
    absorption_auxiliary = absorption_stage(p["scenario"]["forecast_years"], p).auxiliary_mw * flow_ratio if technology == "absorption" else 0.0
    electricity = chiller / cop + fan + pump + absorption_auxiliary
    air_rejection = dry + condenser + fan + pump + absorption_auxiliary
    return electricity, air_rejection


def coupled_npv(p: dict[str, Any], discharge: float, cop: float, capex_multiplier: float, technology: str = "hybrid") -> float:
    plant = p["plant"]
    cost = p["cost"]
    flow_ratio = discharge / p["water"]["discharge_m3_s"]
    rows = []
    previous_installed = 0.0
    for year in range(int(p["scenario"]["horizon_years"]) + 1):
        stage = cooling_stage(float(min(year, p["scenario"]["forecast_years"])), p, technology=technology)
        dry = stage.dry_mw * flow_ratio
        chiller = stage.chiller_mw * flow_ratio
        condenser = chiller * (1.0 + 1.0 / cop)
        total = stage.total_mw * flow_ratio
        pump = 0.0
        if total > 0.0:
            pump = p["water"]["density_kg_m3"] * plant["gravity_m_s2"] * discharge * plant["pump_head_m"] / plant["pump_efficiency"] / 1e6
        fan = plant["dry_auxiliary_fraction"] * (dry + condenser)
        absorption_auxiliary = absorption_stage(float(min(year, p["scenario"]["forecast_years"])), p).auxiliary_mw * flow_ratio if technology == "absorption" else 0.0
        electricity = chiller / cop + fan + pump + absorption_auxiliary
        energy_cost = electricity * HOURS_PER_YEAR * plant["availability"] * plant["electricity_price_eur_mwh"] if year > 0 else 0.0
        installed = capex_multiplier * cumulative_capex_eur(float(min(year, p["scenario"]["forecast_years"])), p, technology)
        investment = max(installed - previous_installed, 0.0)
        previous_installed = installed
        replacement = 0.0
        if year == plant["replacement_year"]:
            replacement = plant["replacement_fraction"] * capex_multiplier * (1.0 + cost["engineering_contingency_fraction"]) * sum(variable_capex_eur(p["scenario"]["forecast_years"], p, technology).values())
        maintenance = plant["maintenance_fraction"] * installed if year > 0 else 0.0
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

    design_p = copy.deepcopy(p)
    design_p["water"]["discharge_m3_s"] = p["hydrology"]["design_discharge_m3_s"]
    design_stage = cooling_stage(final_year, design_p)
    design_electrical = design_electrical_stage(p)
    design_rows = economic_schedule(design_p, "hybrid")
    assert abs(cumulative_capex_eur(final_year, p) - cumulative_capex_eur(final_year, design_p)) < 1e-6
    guard_p = copy.deepcopy(p)
    guard_p["scenario"]["target_temperature_c"] = p["hydrology"]["surface_saturation_c"] - p["hydrology"]["boiling_margin_k"]
    guard_p["hydrology"]["design_discharge_m3_s"] = guard_p["water"]["discharge_m3_s"]
    guard_stage = cooling_stage(final_year, guard_p)
    guard_rows = economic_schedule(guard_p, "hybrid")
    evaporative_stage = cooling_stage(final_year, p, technology="evaporative")
    absorption = absorption_stage(final_year, p)
    absorption_design = design_electrical_stage(p, technology="absorption")
    absorption_economics = alternative_result(p, "absorption", "H8 Absorptionskühlung mit Kompressionsstufe", "Keine Reduktion der Kompressionsstufe im geprüften Temperaturfenster")
    absorption_capex = variable_capex_eur(final_year, p, "absorption")
    absorption_free_p = copy.deepcopy(p)
    absorption_free_p["cost"]["absorption_eur_kw"] = 0.0
    absorption_zero_npv = npv(economic_schedule(absorption_free_p, "absorption"))
    hot_k = absorption.secondary_hot_inlet_c + 273.15
    sink_k = p["plant"]["summer_design_air_c"] + 273.15
    cold_k = s["target_temperature_c"] + 273.15
    absorption_reversible_cop = cold_k / (sink_k - cold_k) * (hot_k - sink_k) / hot_k
    absorption_reversible_outlet = absorption.source_after_generator_c - absorption_reversible_cop * absorption.generator_mw / thermal_capacitance_mw_per_k(p)
    absorption_cop_sensitivity = []
    for thermal_cop in [0.6, 0.7, 0.8, 1.3]:
        varied = copy.deepcopy(p)
        varied["plant"]["absorption_thermal_cop"] = thermal_cop
        varied_stage = absorption_stage(final_year, varied)
        absorption_cop_sensitivity.append({
            "thermal_cop": thermal_cop,
            "evaporator_mw": varied_stage.evaporator_mw,
            "source_after_evaporator_c": varied_stage.source_after_evaporator_c,
            "chiller_mw": varied_stage.chiller_mw,
        })

    alternatives = [
        alternative_result(p, "hybrid", "H1 Zweistufige Vollstromkühlung", "Referenz, dauerhaft innerhalb der Auslegungshülle"),
        alternative_result(p, "evaporative", "H2 Verdunstung mit Kältestufe", "Physikalisch gleichwertig im Szenario, aber Wasserverlust, Hygiene und Stromemissionen"),
        alternative_result(p, "dilution", "H3 Kaltwasserzumischung", "Keine ausreichende Kaltwasserquelle belegt"),
    ]
    hybrid_staged = economic_schedule(p, "hybrid", upfront=False)
    hybrid_upfront = economic_schedule(p, "hybrid", upfront=True)
    evaporation = evaporation_kg_s(evaporative_stage.dry_mw, p)
    evaporation_m3_year = evaporation / p["water"]["density_kg_m3"] * 365 * 24 * 3600
    dilution = dilution_flow_m3_s(final_year, p)
    passive_area = passive_area_m2(final_q, p)
    storage_mw = storage_heating_power_mw(p)
    evaporative_makeup_sensitivity = []
    for cycles in [3.0, 4.0, 5.0]:
        varied = copy.deepcopy(p)
        varied["plant"]["evaporative_cycles_of_concentration"] = cycles
        blowdown_m3 = evaporation_m3_year / (cycles - 1.0)
        drift_m3 = evaporation_m3_year * varied["plant"]["evaporative_drift_fraction"]
        makeup_m3 = evaporation_m3_year + blowdown_m3 + drift_m3
        evaporative_makeup_sensitivity.append({
            "cycles_of_concentration": cycles,
            "evaporation_m3_year": evaporation_m3_year,
            "blowdown_m3_year": blowdown_m3,
            "drift_m3_year": drift_m3,
            "makeup_m3_year": makeup_m3,
            "annual_water_cost_eur": makeup_m3 * varied["cost"]["water_price_eur_m3"],
            "npv_25y_eur": npv(economic_schedule(varied, "evaporative")),
        })

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
    electrical_air_samples = np.array([
        electrical_values_mw(p, float(discharge), float(cop))
        for discharge, cop in zip(discharge_samples, cop_samples)
    ])
    electricity_samples = electrical_air_samples[:, 0]
    air_rejection_samples = electrical_air_samples[:, 1]
    absorption_npv_samples = np.array([
        coupled_npv(p, float(discharge), float(cop), float(capex), technology="absorption")
        for discharge, cop, capex in zip(discharge_samples, cop_samples, capex_samples)
    ])
    absorption_electrical_air_samples = np.array([
        electrical_values_mw(p, float(discharge), float(cop), technology="absorption")
        for discharge, cop in zip(discharge_samples, cop_samples)
    ])
    absorption_electricity_samples = absorption_electrical_air_samples[:, 0]
    absorption_air_rejection_samples = absorption_electrical_air_samples[:, 1]

    availability_scenarios = []
    for availability in [0.95, 0.98, 1.0]:
        varied = copy.deepcopy(p)
        varied["plant"]["availability"] = availability
        rows = economic_schedule(varied, "hybrid", backup_shortfall=True)
        availability_scenarios.append({
            "availability": availability,
            "npv_25y_eur": npv(rows),
            "final_grid_electricity_mwh": rows[final_year]["electricity_mwh"],
            "final_backup_electricity_mwh": rows[final_year]["backup_electricity_mwh"],
            "final_backup_fuel_liters": rows[final_year]["backup_fuel_liters"],
        })

    volume_sensitivity = []
    for volume in [10000.0, 25000.0, 50000.0]:
        varied = copy.deepcopy(p)
        varied["scenario"]["pool_volume_m3"] = volume
        failure = simulate_failure(varied, design_flow_ratio(varied), rtol=1e-11, atol=1e-11, max_step_s=5.0)
        volume_sensitivity.append({
            "effective_pool_volume_m3": volume,
            "failure_time_to_20c_h": failure["failure_time_to_20c_h"],
            "recovery_peak_temperature_c": failure["recovery_peak_temperature_c"],
            "recovery_margin_minutes": failure["recovery_margin_minutes"],
        })

    tariff_scenarios = []
    for tariff in [p["plant"]["electricity_price_eur_mwh"], p["plant"]["electricity_price_high_eur_mwh"]]:
        varied = copy.deepcopy(p)
        varied["plant"]["electricity_price_eur_mwh"] = tariff
        rows = economic_schedule(varied, "hybrid")
        tariff_scenarios.append({"price_eur_mwh": tariff, "npv_25y_eur": npv(rows), "annual_energy_cost_eur": rows[final_year]["energy_cost_eur"]})

    weather_scenarios = []
    for air_temperature in [30.0, 35.0, 38.0]:
        varied = copy.deepcopy(p)
        varied["plant"]["summer_design_air_c"] = air_temperature
        rows = economic_schedule(varied, "hybrid")
        stage = cooling_stage(final_year, varied)
        weather_scenarios.append({"summer_air_c": air_temperature, "electricity_mw": stage.electricity_mw, "npv_25y_eur": npv(rows)})

    years = np.linspace(0.0, 12.0, 481)
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.6))
    axes[0].plot(years, source_temperature_c(years, p), color=BLUE, lw=2)
    axes[0].axhline(s["target_temperature_c"], color=GREEN, ls="--", lw=1)
    axes[0].text(0.4, 14.0, "Regelziel 9 °C", color=GREEN, va="bottom")
    axes[0].axvline(10, color=GRAY, lw=0.8)
    axes[0].set(xlabel="Jahre", ylabel="Szenariotemperatur in °C")
    for fraction, color, label in [(1.0, BLUE, "Gesamtstrom"), (0.01, ORANGE, "1 % Teilstrom"), (0.001, GREEN, "0,1 % Teilstrom")]:
        axes[1].plot(years, required_cooling_mw(years, p, fraction), color=color, lw=2, label=label)
    axes[1].set(xlabel="Jahre", ylabel="Kühlleistung in MW")
    axes[1].set_yscale("symlog", linthresh=1.0)
    axes[1].set_yticks([0.0, 1.0, 10.0, 100.0, 1000.0], ["0", "1", "10", "100", "1000"])
    fig.legend(handles=axes[1].get_lines(), frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(0.5, 0.005))
    fig.subplots_adjust(bottom=0.34, wspace=0.35)
    save_figure(fig, "fig01_prognose_last")

    schedule_years = np.arange(0, 13)
    stages = [cooling_stage(float(year), p) for year in schedule_years]
    fig, ax = plt.subplots(figsize=(8.6, 4.4))
    ax.stackplot(schedule_years, [stage.dry_mw for stage in stages], [stage.chiller_mw for stage in stages], labels=["Trockenkühlung", "Kältemaschinen"], colors=[BLUE, ORANGE], alpha=0.9)
    ax.plot(schedule_years, [stage.total_mw * 1.2 for stage in stages], color=RED, lw=1.8, ls="--", label="Mittelstrom mit 20 % Reserve")
    ax.plot(schedule_years, [stage.total_mw * 1.2 * design_flow_ratio(p) for stage in stages], color=BLUE, lw=1.8, ls="-.", label="p90 mit 20 % Reserve")
    ax.set(xlabel="Jahre", ylabel="Leistung in MW")
    ax.legend(frameon=False, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.24))
    fig.subplots_adjust(bottom=0.36)
    save_figure(fig, "fig02_stufenplan")

    fig, ax = plt.subplots(figsize=(8.6, 4.4))
    for technology, color, label in [("hybrid", BLUE, "H1 Hybrid"), ("evaporative", ORANGE, "H2 Verdunstung")]:
        rows = economic_schedule(p, technology)
        cumulative = np.cumsum([row["present_value_eur"] for row in rows]) / 1e9
        ax.plot([row["year"] for row in rows], cumulative, color=color, lw=2, label=label)
    ax.set(xlabel="Betriebsjahr", ylabel="Barwert in Mrd. €")
    ax.legend(frameon=False, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.24))
    fig.subplots_adjust(bottom=0.34)
    save_figure(fig, "fig03_kostenpfad")

    fig, ax = plt.subplots(figsize=(8.6, 4.4))
    labels = [row["case"] for row in sensitivity]
    values = [row["final_cooling_mw"] for row in sensitivity]
    positions = np.arange(len(labels))
    ax.barh(positions, values, color=[BLUE if value <= final_q else ORANGE for value in values])
    ax.axvline(final_q, color=RED, ls="--", lw=1.4, label=f"Referenz {final_q:.1f} MW".replace(".", ","))
    ax.set_yticks(positions, labels)
    ax.invert_yaxis()
    ax.set(xlabel="Kühlleistung in MW")
    ax.legend(frameon=False, loc="lower right")
    save_figure(fig, "fig04_sensitivitaet")

    fig, axes = plt.subplots(1, 2, figsize=(4.0, 5.0))
    axes[0].hist(q_samples, bins=45, color=BLUE, alpha=0.85)
    mean_line = axes[0].axvline(final_q, color=RED, ls="--", lw=1.4, label="Basis: 877,8")
    reserve_line = axes[0].axvline(final_q * (1 + p["plant"]["reserve_fraction"]), color=GRAY, ls=":", lw=1.6, label="Basis +20 %: 1053,3")
    design_line = axes[0].axvline(design_stage.total_mw * (1 + p["plant"]["reserve_fraction"]), color=BLUE, ls="-.", lw=1.6, label="p90 + 20 %: 2152,5")
    axes[0].set(xlabel="", ylabel="Anzahl", xlim=(0, 2300))
    axes[1].hist(npv_samples / 1e9, bins=45, color=ORANGE, alpha=0.85)
    reference_line = axes[1].axvline(npv(hybrid_staged) / 1e9, color=RED, ls="--", lw=1.4, label=f"Referenz: {npv(hybrid_staged) / 1e9:.2f}".replace(".", ","))
    axes[1].set(xlabel="", ylabel="Anzahl")
    axes[1].xaxis.set_major_formatter(FuncFormatter(lambda value, position: f"{value:g}".replace(".", ",")))
    for ax in axes:
        ax.tick_params(labelsize=20)
        ax.xaxis.label.set_size(20)
        ax.yaxis.label.set_size(20)
    fig.legend(handles=[mean_line, reserve_line, design_line, reference_line], frameon=False, ncol=1, loc="lower center", bbox_to_anchor=(0.5, 0.005), fontsize=20)
    fig.subplots_adjust(bottom=0.43, wspace=0.55)
    save_figure(fig, "fig05_unsicherheit")

    fractions = np.logspace(-4, 0, 200)
    fig, ax = plt.subplots(figsize=(8.6, 4.4))
    ax.loglog(fractions * 100.0, final_q * fractions, color=BLUE, lw=2)
    ax.axhline(storage_mw, color=GREEN, ls="--", label=f"Speichergrenze {storage_mw:.3f} MW".replace(".", ","))
    ax.axvline(1.0, color=ORANGE, ls=":", label="1-%-Teilstrom")
    ax.set(xlabel="Erfasster Strom in %", ylabel="Kühlleistung in MW")
    ax.set_ylim(bottom=0.02)
    ax.set_yticks([0.03, 0.1, 1.0, 10.0, 100.0, 1000.0], ["0,03", "0,1", "1", "10", "100", "1000"])
    ax.legend(frameon=False)
    save_figure(fig, "fig06_teilstrom")

    slide_fig = ROOT / "presentation" / "figures"
    slide_fig.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(6.2, 2.3))
    ax.loglog(fractions * 100.0, final_q * fractions, color=BLUE, lw=2)
    ax.axhline(storage_mw, color=GREEN, ls="--", label="Speicher 0,0303 MW")
    ax.axvline(1.0, color=ORANGE, ls=":", label="1 % Teilstrom")
    ax.set(xlabel="Erfasster Strom in %", ylabel="Kühlleistung in MW")
    ax.set_ylim(bottom=0.02)
    ax.set_yticks([0.03, 0.1, 1.0, 10.0, 100.0, 1000.0], ["0,03", "0,1", "1", "10", "100", "1000"])
    ax.legend(frameon=False, loc="upper left", fontsize=16)
    fig.savefig(slide_fig / "teilstrom.png", dpi=220)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(3.3, 2.3))
    for technology, color, label in [("hybrid", BLUE, "H1 trocken"), ("evaporative", ORANGE, "H2 Verdunstung")]:
        rows = economic_schedule(p, technology)
        cumulative = np.cumsum([row["present_value_eur"] for row in rows]) / 1e9
        ax.plot([row["year"] for row in rows], cumulative, color=color, lw=2)
        ax.text(25.4, cumulative[-1], label.split()[0], color=color, fontsize=16, va="center")
    ax.set(xlabel="Betriebsjahr", ylabel="Barwert in Mrd. €", xlim=(0.0, 27.5))
    fig.savefig(slide_fig / "kostenpfad.png", dpi=220)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(3.4, 2.3))
    ax.hist(q_samples, bins=40, color=BLUE, alpha=0.85)
    ax.axvline(final_q, color=RED, ls="--", lw=1.4)
    ax.axvline(final_q * (1 + p["plant"]["reserve_fraction"]), color=GRAY, ls=":", lw=1.6)
    ax.axvline(design_stage.total_mw * (1 + p["plant"]["reserve_fraction"]), color=BLUE, ls="-.", lw=1.6)
    ax.set(xlabel="Kühlleistung in MW", ylabel="Anzahl", xlim=(200.0, 2300.0), ylim=(0.0, 800.0))
    ax.set_yticks([0.0, 200.0, 400.0, 600.0, 800.0])
    ax.text(final_q, 760.0, "877,8", color=RED, fontsize=16, ha="center", va="bottom")
    ax.text(final_q * (1 + p["plant"]["reserve_fraction"]), 680.0, "1053,3", color=GRAY, fontsize=16, ha="center", va="bottom")
    ax.text(design_stage.total_mw * (1 + p["plant"]["reserve_fraction"]), 760.0, "2152,5", color=BLUE, fontsize=16, ha="right", va="bottom")
    fig.subplots_adjust(left=0.20, right=0.96, top=0.93, bottom=0.23)
    fig.savefig(slide_fig / "unsicherheit.png", dpi=220)
    plt.close(fig)

    results = {
        "model_version": "2.1.0",
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
            "static_overpressure_head_bar": p["plant"]["intake_design_pressure_bar"] - 1.01325,
            "static_overpressure_head_m": (p["plant"]["intake_design_pressure_bar"] - 1.01325) * 1e5 / (p["water"]["density_kg_m3"] * p["plant"]["gravity_m_s2"]),
            "flood_stress_cooling_mw": float(required_cooling_mw(final_year, p) * p["hydrology"]["discharge_flood_m3_s"] / p["water"]["discharge_m3_s"]),
            "return_buffer_m3": p["water"]["discharge_m3_s"] * p["ecology"]["return_buffer_hours"] * 3600.0,
            "module_pipe_diameter_m": float(np.sqrt(4.0 * p["hydrology"]["design_discharge_m3_s"] / p["plant"]["required_modules"] / (np.pi * p["plant"]["module_design_velocity_m_s"]))),
            "reserve_installed_mw": design_stage.total_mw * (1 + p["plant"]["reserve_fraction"]),
            "mean_flow_capacity_mw": final_q * (1 + p["plant"]["reserve_fraction"]),
            "per_module_required_mw": design_stage.total_mw / p["plant"]["required_modules"],
            "per_module_installed_mw": design_stage.total_mw * (1 + p["plant"]["reserve_fraction"]) / p["plant"]["module_count"],
            "storage_lower_bound_mw": storage_mw,
            "evaporation_kg_s": evaporation,
            "evaporation_m3_year": evaporation_m3_year,
            "evaporation_blowdown_m3_year": evaporative_makeup_sensitivity[0]["blowdown_m3_year"],
            "evaporation_drift_m3_year": evaporative_makeup_sensitivity[0]["drift_m3_year"],
            "evaporation_makeup_m3_year": evaporative_makeup_sensitivity[0]["makeup_m3_year"],
            "evaporation_makeup_flow_fraction": evaporative_makeup_sensitivity[0]["makeup_m3_year"] / (365 * 24 * 3600) / p["water"]["discharge_m3_s"],
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
        "design": {
            "flow_m3_s": design_p["water"]["discharge_m3_s"],
            "required_cooling_mw": design_stage.total_mw,
            "dry_cooling_mw": design_stage.dry_mw,
            "chiller_mw": design_stage.chiller_mw,
            "electricity_mw": design_electrical.electricity_mw,
            "condenser_heat_mw": design_electrical.condenser_mw,
            "air_rejection_mw": design_electrical.air_rejection_mw,
            "air_face_area_m2": design_electrical.air_rejection_mw * 1e6 / (p["air"]["face_velocity_m_s"] * p["air"]["density_kg_m3"] * p["air"]["specific_heat_j_kgk"] * p["air"]["temperature_rise_k"]),
            "air_service_area_m2": design_electrical.air_rejection_mw * 1e6 / (p["air"]["face_velocity_m_s"] * p["air"]["density_kg_m3"] * p["air"]["specific_heat_j_kgk"] * p["air"]["temperature_rise_k"]) * p["air"]["service_area_factor"],
            "air_volume_flow_m3_s": design_electrical.air_rejection_mw * 1e6 / (p["air"]["density_kg_m3"] * p["air"]["specific_heat_j_kgk"] * p["air"]["temperature_rise_k"]),
            "installed_capacity_mw": design_stage.total_mw * (1 + p["plant"]["reserve_fraction"]),
            "required_modules": p["plant"]["required_modules"],
            "installed_modules": p["plant"]["module_count"],
            "required_backup_aggregates": int(np.ceil(design_electrical.electricity_mw / p["failure"]["backup_aggregate_capacity_mw"])),
            "installed_backup_aggregates": int(np.ceil(design_electrical.electricity_mw / p["failure"]["backup_aggregate_capacity_mw"])) + 1,
            "backup_fuel_m3": backup_fuel_liters(p) / 1000.0,
            "annual_operating_eur": design_rows[final_year]["net_operation_eur"],
            "npv_25y_eur": npv(design_rows),
        },
        "boil_guard": {
            "target_temperature_c": guard_p["scenario"]["target_temperature_c"],
            "required_cooling_mw": guard_stage.total_mw,
            "electricity_mw": guard_stage.electricity_mw,
            "air_rejection_mw": guard_stage.air_rejection_mw,
            "backup_power_eur": variable_capex_eur(final_year, guard_p)["backup_power"],
            "final_capex_eur": cumulative_capex_eur(final_year, guard_p),
            "npv_25y_eur": npv(guard_rows),
            "ecological_normal_state_preserved": False,
        },
        "alternatives": alternatives,
        "absorption": {
            "thermal_cop": p["plant"]["absorption_thermal_cop"],
            "thermal_cop_source": "HAW [19], einstufige Absorption 0,6 bis 0,8; Sensitivität bis 1,3",
            "auxiliary_fraction": p["plant"]["absorption_auxiliary_fraction"],
            "auxiliary_source": "HAW [19], Beispiel 3 kW elektrisch bei 54 kW Kälte",
            "generator_mw": absorption.generator_mw,
            "evaporator_mw": absorption.evaporator_mw,
            "rejection_mw": absorption.rejection_mw,
            "auxiliary_mw": absorption.auxiliary_mw,
            "dry_cooling_mw": absorption.dry_cooling_mw,
            "chiller_mw": absorption.chiller_mw,
            "condenser_mw": cooling_stage(final_year, p, technology="absorption").condenser_mw,
            "secondary_hot_inlet_c": absorption.secondary_hot_inlet_c,
            "secondary_return_c": absorption.secondary_return_c,
            "secondary_flow_m3_s": absorption.secondary_flow_m3_s,
            "source_after_generator_c": absorption.source_after_generator_c,
            "source_after_evaporator_c": absorption.source_after_evaporator_c,
            "hot_end_approach_k": s["source_temperature_cap_c"] - absorption.secondary_hot_inlet_c,
            "cold_end_approach_k": absorption.source_after_generator_c - absorption.secondary_return_c,
            "reversible_cop": absorption_reversible_cop,
            "reversible_source_after_evaporator_c": absorption_reversible_outlet,
            "thermal_cop_sensitivity": absorption_cop_sensitivity,
            "electricity_mw": absorption_economics["schedule"][final_year]["electricity_mw"],
            "air_rejection_mw": absorption_economics["external_air_rejection_mw"],
            "design_electricity_mw": absorption_design.electricity_mw,
            "design_air_rejection_mw": absorption_design.air_rejection_mw,
            "required_backup_aggregates": int(np.ceil(absorption_design.electricity_mw / p["failure"]["backup_aggregate_capacity_mw"])),
            "installed_backup_aggregates": int(np.ceil(absorption_design.electricity_mw / p["failure"]["backup_aggregate_capacity_mw"])) + 1,
            "backup_fuel_liters": backup_fuel_liters(p, "absorption"),
            "capex_parts_eur": absorption_capex,
            "final_capex_eur": absorption_economics["final_capex_eur"],
            "npv_25y_eur": absorption_economics["npv_25y_eur"],
            "zero_absorption_equipment_npv_eur": absorption_zero_npv,
            "emissions_tco2_year": absorption_economics["emissions_tco2_year"],
            "economics": absorption_economics,
        },
        "evaporative_makeup_sensitivity": evaporative_makeup_sensitivity,
        "flow_fraction_scenarios": flow_fraction_scenarios,
        "availability_scenarios": availability_scenarios,
        "tariff_scenarios": tariff_scenarios,
        "weather_scenarios": weather_scenarios,
        "sensitivity": sensitivity,
        "volume_sensitivity": volume_sensitivity,
        "uncertainty": {
            "sample_count": count,
            "cooling_p05_mw": float(np.quantile(q_samples, 0.05)),
            "cooling_p50_mw": float(np.quantile(q_samples, 0.50)),
            "cooling_p95_mw": float(np.quantile(q_samples, 0.95)),
            "npv_p05_eur": float(np.quantile(npv_samples, 0.05)),
            "npv_p50_eur": float(np.quantile(npv_samples, 0.50)),
            "npv_p95_eur": float(np.quantile(npv_samples, 0.95)),
            "electricity_max_mw": float(np.max(electricity_samples)),
            "electricity_design_limit_mw": design_electrical.electricity_mw,
            "electricity_overload_fraction": float(np.mean(electricity_samples > design_electrical.electricity_mw)),
            "air_rejection_max_mw": float(np.max(air_rejection_samples)),
            "air_rejection_design_limit_mw": design_electrical.air_rejection_mw,
            "air_rejection_overload_fraction": float(np.mean(air_rejection_samples > design_electrical.air_rejection_mw)),
            "absorption_npv_min_delta_eur": float(np.min(absorption_npv_samples - npv_samples)),
            "absorption_electricity_max_mw": float(np.max(absorption_electricity_samples)),
            "absorption_electricity_design_limit_mw": absorption_design.electricity_mw,
            "absorption_electricity_overload_fraction": float(np.mean(absorption_electricity_samples > absorption_design.electricity_mw)),
            "absorption_air_rejection_max_mw": float(np.max(absorption_air_rejection_samples)),
            "absorption_air_rejection_design_limit_mw": absorption_design.air_rejection_mw,
            "absorption_air_rejection_overload_fraction": float(np.mean(absorption_air_rejection_samples > absorption_design.air_rejection_mw)),
            "mean_capacity_overload_fraction": float(np.mean(q_samples > final_q * (1 + p["plant"]["reserve_fraction"]))),
            "design_overload_fraction": float(np.mean(q_samples > design_stage.total_mw * (1 + p["plant"]["reserve_fraction"]))),
            "design_coverage_fraction": float(np.mean(q_samples <= design_stage.total_mw * (1 + p["plant"]["reserve_fraction"]))),
            "coverage_scope": "Nur innerhalb der auf 0,7 bis 4,7 m³/s begrenzten Dreiecksverteilung und des COP-Bereichs 3,0 bis 6,5. Keine Wahrscheinlichkeitsaussage für Extremhochwasser oder andere Wärmequellen.",
        },
        "validation": validation,
        "hybrid_schedule": hybrid_staged,
        "design_schedule": design_rows,
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
    assert np.all(absorption_npv_samples > npv_samples)
    np.savez(OUT / "uncertainty_samples.npz", cooling_mw=q_samples, npv_eur=npv_samples, electricity_mw=electricity_samples, air_rejection_mw=air_rejection_samples, absorption_npv_eur=absorption_npv_samples, absorption_electricity_mw=absorption_electricity_samples, absorption_air_rejection_mw=absorption_air_rejection_samples)

    capex_parts = variable_capex_eur(final_year, p)
    capex_variable = sum(capex_parts.values())
    capex_engineered = capex_variable * (1.0 + p["cost"]["engineering_contingency_fraction"])
    capex_fixed = p["cost"]["fixed_civil_eur"] + p["cost"]["controls_eur"]

    macros = {
        "QFinal": (final_q, 1),
        "QFinalFull": (final_q, 3),
        "DesignCooling": (design_stage.total_mw, 1),
        "DesignElectric": (design_electrical.electricity_mw, 1),
        "DesignAirRejection": (design_electrical.air_rejection_mw, 1),
        "DesignNpv": (npv(design_rows) / 1e9, 3),
        "DesignOpex": (design_rows[final_year]["net_operation_eur"] / 1e6, 1),
        "GuardTarget": (guard_p["scenario"]["target_temperature_c"], 2),
        "GuardCooling": (guard_stage.total_mw, 1),
        "GuardElectric": (guard_stage.electricity_mw, 2),
        "GuardCapex": (cumulative_capex_eur(final_year, guard_p) / 1e6, 1),
        "GuardNpv": (npv(guard_rows) / 1e9, 3),
        "KDurchfluss": (thermal_capacitance_mw_per_k(p), 3),
        "QDry": (final_stage.dry_mw, 1),
        "QChiller": (final_stage.chiller_mw, 1),
        "QChillerFull": (final_stage.chiller_mw, 3),
        "PElectric": (final_stage.electricity_mw, 1),
        "EElectric": (final_stage.electricity_mw * HOURS_PER_YEAR / 1000, 1),
        "PChiller": (final_stage.chiller_mw / p["plant"]["chiller_cop"], 3),
        "PFans": (p["plant"]["dry_auxiliary_fraction"] * (final_stage.dry_mw + final_stage.condenser_mw), 3),
        "PPumps": (final_stage.electricity_mw - final_stage.chiller_mw / p["plant"]["chiller_cop"] - p["plant"]["dry_auxiliary_fraction"] * (final_stage.dry_mw + final_stage.condenser_mw), 3),
        "EnergyCostFinal": (hybrid_staged[final_year]["energy_cost_eur"] / 1e6, 2),
        "MaintenanceFinal": (hybrid_staged[final_year]["maintenance_eur"] / 1e6, 2),
        "QCondenser": (final_stage.condenser_mw, 1),
        "QAirRejection": (final_stage.air_rejection_mw, 1),
        "AirFaceArea": (results["design"]["air_face_area_m2"], 0),
        "AirServiceArea": (results["design"]["air_service_area_m2"] / 10000, 2),
        "AirVolumeFlow": (results["design"]["air_volume_flow_m3_s"], 0),
        "EmissionsHybrid": (results["baseline"]["emissions_tco2_year"] / 1000, 1),
        "EmissionsEvap": (alternatives[1]["emissions_tco2_year"] / 1000, 1),
        "EmissionsDelta": ((results["baseline"]["emissions_tco2_year"] - alternatives[1]["emissions_tco2_year"]) / 1000, 1),
        "FuelReserve": (results["baseline"]["backup_fuel_liters"] / 1e6, 3),
        "DieselVolume": (results["design"]["backup_fuel_m3"], 0),
        "ReturnRampHours": (results["baseline"]["return_ramp_hours"], 0),
        "ReturnRampRate": (results["baseline"]["return_ramp_max_rate_k_h"], 1),
        "RecoveryPeak": (validation["recovery_peak_temperature_c"], 1),
        "RecoveryMargin": (validation["recovery_margin_minutes"], 1),
        "RecoveryPeakNinety": (validation["failure_p90"]["recovery_peak_temperature_c"], 1),
        "FailureMinutesNinety": (validation["failure_p90"]["failure_time_to_20c_h"] * 60, 1),
        "RecoveryMarginNinety": (validation["failure_p90"]["recovery_margin_minutes"], 1),
        "MeanCapacity": (results["baseline"]["mean_flow_capacity_mw"], 1),
        "StaticHead": (results["baseline"]["static_overpressure_head_m"], 1),
        "AvailabilityLowNpv": (availability_scenarios[0]["npv_25y_eur"] / 1e9, 2),
        "AvailabilityHighNpv": (availability_scenarios[-1]["npv_25y_eur"] / 1e9, 2),
        "TariffHighNpv": (tariff_scenarios[-1]["npv_25y_eur"] / 1e9, 3),
        "WeatherHighNpv": (weather_scenarios[-1]["npv_25y_eur"] / 1e9, 2),
        "QFloodStress": (results["baseline"]["flood_stress_cooling_mw"] / 1000, 2),
        "BufferVolume": (results["baseline"]["return_buffer_m3"], 0),
        "PipeDiameter": (results["baseline"]["module_pipe_diameter_m"], 2),
        "QReserve": (results["baseline"]["reserve_installed_mw"], 1),
        "QModule": (results["baseline"]["per_module_required_mw"], 1),
        "QModuleInstalled": (results["baseline"]["per_module_installed_mw"], 1),
        "QStorage": (storage_mw, 4),
        "EvapRate": (evaporation, 1),
        "EvapDry": (evaporative_stage.dry_mw, 1),
        "EvapChiller": (evaporative_stage.chiller_mw, 1),
        "EvapAnnual": (evaporation / p["water"]["density_kg_m3"] * 365 * 24 * 3600 / 1e6, 2),
        "EvapFraction": (100 * evaporation / p["water"]["density_kg_m3"] / p["water"]["discharge_m3_s"], 1),
        "EvapMakeupAnnual": (evaporative_makeup_sensitivity[0]["makeup_m3_year"] / 1e6, 2),
        "EvapBlowdownAnnual": (evaporative_makeup_sensitivity[0]["blowdown_m3_year"] / 1e6, 2),
        "EvapMakeupFraction": (100 * results["baseline"]["evaporation_makeup_flow_fraction"], 1),
        "EvapCycles": (p["plant"]["evaporative_cycles_of_concentration"], 0),
        "EvapDriftPercent": (100 * p["plant"]["evaporative_drift_fraction"], 2),
        "EvapMakeupLow": (evaporative_makeup_sensitivity[-1]["makeup_m3_year"] / 1e6, 2),
        "EvapMakeupHigh": (evaporative_makeup_sensitivity[0]["makeup_m3_year"] / 1e6, 2),
        "DilutionFlow": (dilution, 1),
        "DilutionRatio": (dilution / p["water"]["discharge_m3_s"], 1),
        "PassiveArea": (passive_area / 1e6, 1),
        "CapexFinal": (cumulative_capex_eur(final_year, p, "hybrid") / 1e6, 0),
        "OpexFinal": (hybrid_staged[final_year]["net_operation_eur"] / 1e6, 1),
        "NpvHybrid": (npv(hybrid_staged) / 1e9, 2),
        "NpvHybridFull": (npv(hybrid_staged) / 1e9, 3),
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
        "MeanOverloadPercent": (100 * results["uncertainty"]["mean_capacity_overload_fraction"], 2),
        "DesignOverloadPercent": (100 * results["uncertainty"]["design_overload_fraction"], 1),
        "McDischargeLow": (p["uncertainty"]["discharge_low_m3_s"], 1),
        "McDischargeMode": (p["uncertainty"]["discharge_mode_m3_s"], 1),
        "McDischargeHigh": (p["uncertainty"]["discharge_high_m3_s"], 1),
        "McCopLow": (p["uncertainty"]["cop_low"], 1),
        "McCopMode": (p["uncertainty"]["cop_mode"], 1),
        "McCopHigh": (p["uncertainty"]["cop_high"], 1),
        "McCapexSigma": (p["uncertainty"]["capex_multiplier_sigma"], 2),
        "McSeed": (p["uncertainty"]["random_seed"], 0),
        "EvapSourceOutlet": (p["plant"]["evaporative_source_outlet_c"], 0),
        "EvapSecondaryInlet": (p["plant"]["evaporative_secondary_inlet_c"], 0),
        "EvapSecondaryOutlet": (p["plant"]["evaporative_secondary_outlet_c"], 0),
        "EvapSecondaryFlow": (p["plant"]["evaporative_secondary_flow_m3_s"], 1),
        "CapexExchanger": (capex_parts["exchanger"] / 1e6, 1),
        "CapexChiller": (capex_parts["chiller"] / 1e6, 1),
        "CapexDryCooler": (capex_parts["dry_cooler"] / 1e6, 1),
        "CapexBackup": (capex_parts["backup_power"] / 1e6, 1),
        "CapexVariable": (capex_variable / 1e6, 1),
        "CapexEngineered": (capex_engineered / 1e6, 1),
        "CapexFixed": (capex_fixed / 1e6, 1),
        "BackupRequired": (results["design"]["required_backup_aggregates"], 0),
        "BackupInstalled": (results["design"]["installed_backup_aggregates"], 0),
        "BackupAggregateCapacity": (p["failure"]["backup_aggregate_capacity_mw"], 0),
        "ElectricityOverloadPercent": (100 * results["uncertainty"]["electricity_overload_fraction"], 2),
        "AirRejectionOverloadPercent": (100 * results["uncertainty"]["air_rejection_overload_fraction"], 2),
        "VolumeMarginLow": (volume_sensitivity[0]["recovery_margin_minutes"], 2),
        "VolumeMarginHigh": (volume_sensitivity[-1]["recovery_margin_minutes"], 2),
        "AvailabilityBackupFuel": (availability_scenarios[0]["final_backup_fuel_liters"] / 1e6, 2),
        "LegacyEscalationPercent": (100 * (p["cost"]["legacy_escalation_factor"] - 1.0), 0),
        "VolumePeakLow": (volume_sensitivity[0]["recovery_peak_temperature_c"], 1),
        "ElectricitySampleMax": (results["uncertainty"]["electricity_max_mw"], 1),
        "AirRejectionSampleMax": (results["uncertainty"]["air_rejection_max_mw"], 1),
        "AbsGenerator": (absorption.generator_mw, 1),
        "AbsEvaporator": (absorption.evaporator_mw, 1),
        "AbsRejection": (absorption.rejection_mw, 1),
        "AbsDryCooling": (absorption.dry_cooling_mw, 1),
        "AbsChiller": (absorption.chiller_mw, 1),
        "AbsCondenser": (cooling_stage(final_year, p, technology="absorption").condenser_mw, 1),
        "AbsAuxiliary": (absorption.auxiliary_mw, 2),
        "AbsAuxPercent": (100 * p["plant"]["absorption_auxiliary_fraction"], 2),
        "AbsHotInlet": (absorption.secondary_hot_inlet_c, 0),
        "AbsHotReturn": (absorption.secondary_return_c, 0),
        "AbsSourceAfterGenerator": (absorption.source_after_generator_c, 0),
        "AbsSourceAfterEvaporator": (absorption.source_after_evaporator_c, 1),
        "AbsSecondaryFlow": (absorption.secondary_flow_m3_s, 1),
        "AbsThermalCop": (p["plant"]["absorption_thermal_cop"], 2),
        "AbsRevCop": (absorption_reversible_cop, 2),
        "AbsRevOutlet": (absorption_reversible_outlet, 1),
        "AbsCopHighOutlet": (absorption_cop_sensitivity[-1]["source_after_evaporator_c"], 1),
        "AbsElectricity": (absorption_economics["schedule"][final_year]["electricity_mw"], 1),
        "AbsDesignElectricity": (absorption_design.electricity_mw, 1),
        "AbsAirRejection": (absorption_economics["external_air_rejection_mw"], 1),
        "AbsCapex": (absorption_economics["final_capex_eur"] / 1e6, 1),
        "AbsNpv": (absorption_economics["npv_25y_eur"] / 1e9, 3),
        "AbsZeroNpv": (absorption_zero_npv / 1e9, 3),
        "AbsEmissions": (absorption_economics["emissions_tco2_year"] / 1000, 1),
        "AbsFuel": (backup_fuel_liters(p, "absorption") / 1e6, 3),
        "AbsRequiredBackup": (int(np.ceil(absorption_design.electricity_mw / p["failure"]["backup_aggregate_capacity_mw"])), 0),
        "AbsInstalledBackup": (int(np.ceil(absorption_design.electricity_mw / p["failure"]["backup_aggregate_capacity_mw"])) + 1, 0),
        "AbsMinNpvDelta": (results["uncertainty"]["absorption_npv_min_delta_eur"] / 1e6, 1),
        "AbsElectricitySampleMax": (results["uncertainty"]["absorption_electricity_max_mw"], 1),
        "AbsOverloadPercent": (100 * results["uncertainty"]["absorption_electricity_overload_fraction"], 2),
    }
    with (GEN / "numbers.tex").open("w", encoding="utf-8") as handle:
        for name, (value, digits) in macros.items():
            handle.write(macro(name, value, digits))

    with (GEN / "alternatives.tex").open("w", encoding="utf-8") as handle:
        handle.write("\\begin{tabular}{@{}p{51mm}rrr@{}}\n\\toprule\nGröße im Auslegungsjahr & H1 Hybrid & H2 Verdunstung & H3 Zumischung \\\\\n\\midrule\n")
        rows = [
            ("Kühlleistung (Wärmeentzug) in MW", "required_cooling_mw", 1.0, 1),
            ("Investition in Mio. €", "installed_capex_eur", 1e6, 1),
            ("Elektrische Leistung in MW", "electricity_mw", 1.0, 1),
            ("Strom pro Jahr in GWh", "electricity_mwh", 1000.0, 1),
            ("Betriebskosten in Mio. €", "net_operation_eur", 1e6, 1),
        ]
        for label, key, scale, digits in rows:
            values = [f"{alt['schedule'][final_year][key] / scale:.{digits}f}".replace(".", ",") for alt in alternatives]
            handle.write(f"{label} & {' & '.join(values)} \\\\\n")
        air_values = [f"{alt['external_air_rejection_mw']:.1f}".replace(".", ",") for alt in alternatives]
        handle.write("Davon Wärmeabgabe an Luft in MW & " + " & ".join(air_values) + " \\\\\n")
        handle.write("Zusatzwasser H2/H3 & 0 m³ & ")
        handle.write(f"{alternatives[1]['annual_water_m3']/1e6:.2f}".replace(".", ",") + " Mio. m³ & " + f"{alternatives[2]['annual_water_m3']/1e9:.3f}".replace(".", ",") + " Mrd. m³ \\\\\n")
        npv_values = [f"{alt['npv_25y_eur']/1e9:.3f}".replace(".", ",") for alt in alternatives]
        handle.write("Barwert in Mrd. € & " + " & ".join(npv_values) + " \\\\\n")
        handle.write("\\bottomrule\n\\end{tabular}\n")

    with (GEN / "absorption.tex").open("w", encoding="utf-8") as handle:
        handle.write("\\begin{tabular*}{\\columnwidth}{@{\\extracolsep{\\fill}}>{\\hspace{0pt}\\raggedright\\arraybackslash}p{40mm}rr}\n\\toprule\nGröße & H1 & H8 \\\\\n\\midrule\n")
        rows = [
            ("Generatorwärme in MW", 0.0, absorption.generator_mw, 1.0, 1),
            ("Verdampferkälte in MW", 0.0, absorption.evaporator_mw, 1.0, 1),
            ("Direkte Trockenkühlung in MW", final_stage.dry_mw, absorption.dry_cooling_mw, 1.0, 1),
            ("Kompressionskälte in MW", final_stage.chiller_mw, absorption.chiller_mw, 1.0, 1),
            ("Kondensatorwärme in MW", final_stage.condenser_mw, cooling_stage(final_year, p, technology="absorption").condenser_mw, 1.0, 1),
            ("Absorptionsabwärme in MW", 0.0, absorption.rejection_mw, 1.0, 1),
            ("Elektrik im Mittelbetrieb in MW", final_stage.electricity_mw, absorption_economics["schedule"][final_year]["electricity_mw"], 1.0, 1),
            ("Elektrik bei COP 3,0 in MW", design_electrical.electricity_mw, absorption_design.electricity_mw, 1.0, 1),
            ("Wärmeabgabe im Mittelbetrieb in MW", final_stage.air_rejection_mw, absorption_economics["external_air_rejection_mw"], 1.0, 1),
            ("Investition in Mio. €", cumulative_capex_eur(final_year, p, "hybrid"), absorption_economics["final_capex_eur"], 1e6, 1),
            ("Barwert in Mrd. €", npv(hybrid_staged), absorption_economics["npv_25y_eur"], 1e9, 3),
            ("Emissionen in kt CO₂ pro Jahr", results["baseline"]["emissions_tco2_year"], absorption_economics["emissions_tco2_year"], 1000.0, 1),
            ("Diesel für 48 Stunden in Mio. Liter", results["baseline"]["backup_fuel_liters"], backup_fuel_liters(p, "absorption"), 1e6, 3),
        ]
        for label, reference, variant, scale, digits in rows:
            reference_value = f"{reference / scale:.{digits}f}".replace(".", ",")
            variant_value = f"{variant / scale:.{digits}f}".replace(".", ",")
            handle.write(f"{label} & {reference_value} & {variant_value} \\\\\n")
        handle.write("\\bottomrule\n\\end{tabular*}\n")

    with (GEN / "sensitivity.tex").open("w", encoding="utf-8") as handle:
        handle.write("\\begin{tabular*}{\\columnwidth}{@{\\extracolsep{\\fill}}>{\\hspace{0pt}\\raggedright\\arraybackslash}p{24mm}rrr}\n\\toprule\nFall & MW & \\% & Mrd. € \\\\\n\\midrule\n")
        for row in sensitivity:
            label = row["case"].replace("%", "\\%")
            handle.write(f"{label} & {row['final_cooling_mw']:.1f} & {100*row['relative_change']:+.1f} & {row['npv_25y_eur']/1e9:.3f} \\\\\n".replace(".", ","))
        handle.write("\\bottomrule\n\\end{tabular*}\n")

    with (GEN / "flow_fractions.tex").open("w", encoding="utf-8") as handle:
        handle.write("\\begin{tabular*}{\\columnwidth}{@{\\extracolsep{\\fill}}lrrrr}\n\\toprule\nAnteil & MW & MW & Mio. € & Mrd. € \\\\\n\\midrule\n")
        for row in flow_fraction_scenarios:
            handle.write(f"{100*row['affected_fraction']:.1f} \\% & {row['final_cooling_mw']:.1f} & {row['electricity_mw']:.2f} & {row['final_capex_eur']/1e6:.0f} & {row['npv_25y_eur']/1e9:.3f} \\\\\n".replace(".", ","))
        handle.write("\\bottomrule\n\\end{tabular*}\n")

    manifest = {}
    manifest_paths = [
        ROOT / "data" / "parameters.yml",
        ROOT / "data" / "nist_saturation_32_100.tsv",
        ROOT / "requirements.lock.txt",
        ROOT / "Makefile",
        *sorted((ROOT / "model").glob("*.py")),
        *sorted((ROOT / "scripts").glob("*.py")),
        *sorted((ROOT / "scripts").glob("*.sh")),
        OUT / "results.json",
        OUT / "hybrid_schedule.csv",
        OUT / "sensitivity.csv",
        OUT / "uncertainty_samples.npz",
        *sorted(GEN.glob("*.tex")),
        *sorted(FIG.glob("fig*.pdf")),
        *sorted(FIG.glob("fig*.png")),
        *sorted((ROOT / "presentation" / "figures").glob("*.png")),
    ]
    for path in manifest_paths:
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
