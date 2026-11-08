from __future__ import annotations

from typing import Any

import numpy as np
from scipy.integrate import solve_ivp

from core import (
    HOURS_PER_YEAR,
    SECONDS_PER_YEAR,
    absorption_stage,
    backup_fuel_liters,
    variable_capex_eur,
    cooling_stage,
    design_electrical_stage,
    dilution_flow_m3_s,
    dry_outlet_temperature_c,
    economic_schedule,
    evaporation_kg_s,
    heating_rate_k_per_year,
    npv,
    planned_return_temperature_c,
    required_cooling_mw,
    source_temperature_c,
    storage_heating_power_mw,
    thermal_capacitance_mw_per_k,
)


def simulate_failure(p: dict[str, Any], flow_ratio: float, rtol: float = 1e-9, atol: float = 1e-9, max_step_s: float | None = None) -> dict[str, float | int]:
    s = p["scenario"]
    w = p["water"]
    f = p["failure"]
    tau_s = s["pool_volume_m3"] / (w["discharge_m3_s"] * s["affected_flow_fraction"] * flow_ratio)
    cooling_mw = float(required_cooling_mw(s["forecast_years"], p, affected_fraction=flow_ratio))
    source = s["boiling_temperature_c"]
    initial = s["initial_temperature_c"]
    start_s = (f["detection_minutes"] + f["generator_start_minutes"]) * 60.0
    full_s = (f["detection_minutes"] + f["full_cooling_minutes"]) * 60.0
    assert 0.0 < f["detection_minutes"] * 60.0 < start_s < full_s <= f["controls_ups_minutes"] * 60.0
    failure_time_h = -tau_s * np.log((source - 20.0) / (source - initial)) / 3600.0

    def recovered_cooling(time_s: float, temperature: list[float]) -> list[float]:
        fraction = min(max((time_s - start_s) / (full_s - start_s), 0.0), 1.0)
        source_gain = (source - temperature[0]) / tau_s
        cooling_loss = cooling_mw * 1e6 / (w["density_kg_m3"] * s["pool_volume_m3"] * w["specific_heat_j_kgk"]) * fraction
        return [source_gain - cooling_loss]

    end_s = max(failure_time_h * 3600.0 * 1.2, full_s * 1.2)
    time_s = np.unique(np.concatenate([np.linspace(0.0, end_s, 1001), [start_s, full_s]]))
    options: dict[str, Any] = {"rtol": rtol, "atol": atol}
    if max_step_s is not None:
        options["max_step"] = max_step_s
    peak_temperature = initial
    for segment_start, segment_end in [(0.0, start_s), (start_s, full_s), (full_s, end_s)]:
        segment_points = time_s[(time_s >= segment_start) & (time_s <= segment_end)]
        recovery = solve_ivp(recovered_cooling, (segment_start, segment_end), [initial], t_eval=segment_points, **options)
        if not recovery.success:
            raise RuntimeError(f"Ausfallintegration fehlgeschlagen: {recovery.message}")
        peak_temperature = max(peak_temperature, float(np.max(recovery.y[0])))
        initial = float(recovery.y[0, -1])
    return {
        "flow_ratio": flow_ratio,
        "pool_time_constant_h": tau_s / 3600.0,
        "failure_time_to_20c_h": float(failure_time_h),
        "recovery_peak_temperature_c": peak_temperature,
        "recovery_margin_minutes": float(failure_time_h * 60.0 - full_s / 60.0),
        "detection_minutes": f["detection_minutes"],
        "generator_start_minutes": f["generator_start_minutes"],
        "full_cooling_minutes": f["full_cooling_minutes"],
        "cooling_start_absolute_minutes": start_s / 60.0,
        "full_cooling_absolute_minutes": full_s / 60.0,
        "evaluation_points": len(time_s),
    }


def run_validation(p: dict[str, Any]) -> dict[str, float | bool]:
    s = p["scenario"]
    w = p["water"]
    final_year = s["forecast_years"]
    final_q = float(required_cooling_mw(final_year, p))
    expected_q = thermal_capacitance_mw_per_k(p) * (s["boiling_temperature_c"] - s["target_temperature_c"])
    assert abs(final_q - expected_q) < 1e-9
    assert abs(float(source_temperature_c(final_year, p)) - s["boiling_temperature_c"]) < 1e-12
    assert abs(heating_rate_k_per_year(p) - 9.1) < 1e-12

    stage = cooling_stage(final_year, p)
    assert abs(stage.dry_mw + stage.chiller_mw - stage.total_mw) < 1e-9
    assert abs(stage.air_rejection_mw - stage.total_mw - stage.electricity_mw) < 1e-9
    assert abs(stage.condenser_mw - stage.chiller_mw * (1.0 + 1.0 / p["plant"]["chiller_cop"])) < 1e-9
    assert stage.electricity_mw > 0.0
    assert stage.total_mw * 1000.0 * (1.0 + p["plant"]["reserve_fraction"]) >= final_q * 1000.0

    evaporation = evaporation_kg_s(final_q, p)
    assert abs(evaporation * w["latent_heat_j_kg"] / 1e6 - final_q) < 1e-9

    cold_flow = dilution_flow_m3_s(final_year, p)
    hot_flow = w["discharge_m3_s"] * s["affected_flow_fraction"]
    mixed = (hot_flow * s["boiling_temperature_c"] + cold_flow * w["cold_dilution_temperature_c"]) / (hot_flow + cold_flow)
    assert abs(mixed - s["target_temperature_c"]) < 1e-9

    storage_mw = storage_heating_power_mw(p)
    storage_check = w["density_kg_m3"] * s["pool_volume_m3"] * w["specific_heat_j_kgk"] * heating_rate_k_per_year(p) / SECONDS_PER_YEAR / 1e6
    assert abs(storage_mw - storage_check) < 1e-12

    k = thermal_capacitance_mw_per_k(p)
    tau_s = s["pool_volume_m3"] / (w["discharge_m3_s"] * s["affected_flow_fraction"])
    t_eval = np.linspace(0.0, 6.0 * tau_s, 80)
    source = 40.0
    initial = 9.0

    def rhs(time: float, temperature: list[float]) -> list[float]:
        return [(source - temperature[0]) / tau_s]

    numerical = solve_ivp(rhs, (0.0, float(t_eval[-1])), [initial], t_eval=t_eval, rtol=1e-10, atol=1e-10)
    analytical = source + (initial - source) * np.exp(-t_eval / tau_s)
    ode_error_k = float(np.max(np.abs(numerical.y[0] - analytical)))
    assert ode_error_k < 1e-6

    f = p["failure"]
    design_electricity = design_electrical_stage(p).electricity_mw
    aggregate_capacity = f["backup_aggregate_capacity_mw"]
    required_aggregates = int(np.ceil(design_electricity / aggregate_capacity))
    assert required_aggregates > 0
    assert required_aggregates * aggregate_capacity >= design_electricity
    assert (required_aggregates - 1) * aggregate_capacity < design_electricity
    design_ratio = p["hydrology"]["design_discharge_m3_s"] / w["discharge_m3_s"]
    failure_mean = simulate_failure(p, 1.0)
    failure_p90 = simulate_failure(p, design_ratio, rtol=1e-11, atol=1e-11, max_step_s=5.0)
    failure_p90_coarse = simulate_failure(p, design_ratio, rtol=1e-9, atol=1e-9, max_step_s=30.0)
    failure_p90_convergence_error_k = abs(failure_p90["recovery_peak_temperature_c"] - failure_p90_coarse["recovery_peak_temperature_c"])
    for failure_case in (failure_mean, failure_p90):
        assert failure_case["failure_time_to_20c_h"] > 0.0
        assert failure_case["recovery_peak_temperature_c"] < 20.0
        assert failure_case["recovery_margin_minutes"] > 0.0
    assert failure_p90_convergence_error_k < 1e-6

    hybrid_staged = economic_schedule(p, "hybrid", upfront=False)
    hybrid_upfront = economic_schedule(p, "hybrid", upfront=True)
    assert npv(hybrid_upfront) > npv(hybrid_staged)
    assert hybrid_staged[-1]["required_cooling_mw"] == expected_q
    assert abs(hybrid_staged[10]["electricity_mwh"] / HOURS_PER_YEAR - hybrid_staged[10]["electricity_mw"]) < 1e-9
    expected_replacement = p["plant"]["replacement_fraction"] * (1.0 + p["cost"]["engineering_contingency_fraction"]) * sum(variable_capex_eur(final_year, p).values())
    assert abs(hybrid_staged[p["plant"]["replacement_year"]]["replacement_eur"] - expected_replacement) < 1e-6
    e = p["ecology"]
    ramp_hours = (e["ramp_stress_start_c"] - s["target_temperature_c"]) / e["maximum_return_rate_k_h"]
    ramp_time_h = np.linspace(0.0, ramp_hours + 1.0, 921)
    ramp_temperature_c = planned_return_temperature_c(ramp_time_h, p)
    ramp_max_rate_k_h = float(np.max(np.abs(np.diff(ramp_temperature_c) / np.diff(ramp_time_h))))
    assert abs(ramp_hours - 91.0) < 1e-12
    assert ramp_max_rate_k_h <= e["maximum_return_rate_k_h"] + 1e-12
    assert ramp_temperature_c[-1] == s["target_temperature_c"]
    expected_fuel = design_electrical_stage(p).electricity_mw * 1000.0 * p["plant"]["backup_duration_hours"] / (p["plant"]["backup_thermal_efficiency"] * p["plant"]["diesel_energy_kwh_l"])
    assert abs(backup_fuel_liters(p) - expected_fuel) < 1e-9
    evaporative = cooling_stage(final_year, p, technology="evaporative")
    assert abs(evaporative.dry_mw + evaporative.chiller_mw - evaporative.total_mw) < 1e-9
    assert evaporative.chiller_mw > 0.0 and evaporative.electricity_mw > 0.0
    assert abs(evaporation_kg_s(evaporative.dry_mw, p) * w["latent_heat_j_kg"] / 1e6 - evaporative.dry_mw) < 1e-9

    absorption = absorption_stage(final_year, p)
    absorption_electric = cooling_stage(final_year, p, technology="absorption")
    secondary_heat = absorption.secondary_flow_m3_s * w["density_kg_m3"] * w["specific_heat_j_kgk"] * (absorption.secondary_hot_inlet_c - absorption.secondary_return_c) / 1e6
    assert abs(secondary_heat - absorption.generator_mw) < 1e-9
    assert abs(absorption.generator_mw + absorption.evaporator_mw + absorption.dry_cooling_mw + absorption.chiller_mw - absorption.total_mw) < 1e-9
    assert abs(absorption_electric.air_rejection_mw - absorption_electric.total_mw - absorption_electric.electricity_mw) < 1e-9
    assert s["source_temperature_cap_c"] - absorption.secondary_hot_inlet_c > 0.0
    assert absorption.source_after_generator_c - absorption.secondary_return_c > 0.0
    for thermal_cop in [0.6, 0.7, 0.8, 1.3]:
        varied = dict(p, plant=dict(p["plant"], absorption_thermal_cop=thermal_cop))
        varied_absorption = absorption_stage(final_year, varied)
        assert varied_absorption.source_after_evaporator_c > dry_outlet_temperature_c(p)
        assert abs(varied_absorption.chiller_mw - stage.chiller_mw) < 1e-9
    hot_k = absorption.secondary_hot_inlet_c + 273.15
    sink_k = p["plant"]["summer_design_air_c"] + 273.15
    cold_k = s["target_temperature_c"] + 273.15
    reversible_cop = cold_k / (sink_k - cold_k) * (hot_k - sink_k) / hot_k
    reversible_outlet = absorption.source_after_generator_c - reversible_cop * absorption.generator_mw / thermal_capacitance_mw_per_k(p)
    assert reversible_outlet > dry_outlet_temperature_c(p)

    return {
        "replacement_error_eur": abs(hybrid_staged[p["plant"]["replacement_year"]]["replacement_eur"] - expected_replacement),
        "return_ramp_hours": ramp_hours,
        "return_ramp_max_rate_k_h": ramp_max_rate_k_h,
        "backup_fuel_liters": backup_fuel_liters(p),
        "energy_balance_error_mw": abs(final_q - expected_q),
        "stage_split_error_mw": abs(stage.dry_mw + stage.chiller_mw - stage.total_mw),
        "heat_sink_balance_error_mw": abs(stage.air_rejection_mw - stage.total_mw - stage.electricity_mw),
        "evaporation_balance_error_mw": abs(evaporation * w["latent_heat_j_kg"] / 1e6 - final_q),
        "evaporative_stage_error_mw": abs(evaporative.dry_mw + evaporative.chiller_mw - evaporative.total_mw),
        "absorption_secondary_balance_error_mw": abs(secondary_heat - absorption.generator_mw),
        "absorption_stage_error_mw": abs(absorption.generator_mw + absorption.evaporator_mw + absorption.dry_cooling_mw + absorption.chiller_mw - absorption.total_mw),
        "absorption_heat_sink_error_mw": abs(absorption_electric.air_rejection_mw - absorption_electric.total_mw - absorption_electric.electricity_mw),
        "absorption_reversible_cop": reversible_cop,
        "absorption_reversible_outlet_c": reversible_outlet,
        "dilution_mixing_error_c": abs(mixed - s["target_temperature_c"]),
        "ode_max_error_k": ode_error_k,
        "pool_time_constant_h": tau_s / 3600.0,
        "failure_time_to_20c_h": failure_mean["failure_time_to_20c_h"],
        "recovery_peak_temperature_c": failure_mean["recovery_peak_temperature_c"],
        "recovery_margin_minutes": failure_mean["recovery_margin_minutes"],
        "failure_mean": failure_mean,
        "failure_p90": failure_p90,
        "failure_p90_convergence_error_k": failure_p90_convergence_error_k,
        "staged_npv_lower_than_upfront": npv(hybrid_staged) < npv(hybrid_upfront),
        "all_checks_passed": True,
    }
