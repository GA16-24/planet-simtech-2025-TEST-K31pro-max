from __future__ import annotations

from typing import Any

import numpy as np
from scipy.integrate import solve_ivp

from core import (
    HOURS_PER_YEAR,
    SECONDS_PER_YEAR,
    cooling_stage,
    dilution_flow_m3_s,
    economic_schedule,
    evaporation_kg_s,
    heating_rate_k_per_year,
    npv,
    required_cooling_mw,
    source_temperature_c,
    storage_heating_power_mw,
    thermal_capacitance_mw_per_k,
)


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

    failure_source = s["boiling_temperature_c"]
    failure_time_20c_h = -tau_s * np.log((failure_source - 20.0) / (failure_source - initial)) / 3600.0
    assert failure_time_20c_h > 0.0

    hybrid_staged = economic_schedule(p, "hybrid", upfront=False)
    hybrid_upfront = economic_schedule(p, "hybrid", upfront=True)
    assert npv(hybrid_upfront) > npv(hybrid_staged)
    assert hybrid_staged[-1]["required_cooling_mw"] == expected_q
    assert abs(hybrid_staged[10]["electricity_mwh"] / HOURS_PER_YEAR - hybrid_staged[10]["electricity_mw"]) < 1e-9

    return {
        "energy_balance_error_mw": abs(final_q - expected_q),
        "stage_split_error_mw": abs(stage.dry_mw + stage.chiller_mw - stage.total_mw),
        "heat_sink_balance_error_mw": abs(stage.air_rejection_mw - stage.total_mw - stage.electricity_mw),
        "evaporation_balance_error_mw": abs(evaporation * w["latent_heat_j_kg"] / 1e6 - final_q),
        "dilution_mixing_error_c": abs(mixed - s["target_temperature_c"]),
        "ode_max_error_k": ode_error_k,
        "pool_time_constant_h": tau_s / 3600.0,
        "failure_time_to_20c_h": float(failure_time_20c_h),
        "staged_npv_lower_than_upfront": npv(hybrid_staged) < npv(hybrid_upfront),
        "all_checks_passed": True,
    }
