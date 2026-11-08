from __future__ import annotations

import copy
import unittest

import yaml

import numpy as np

from core import backup_fuel_cost_eur, backup_fuel_liters, cooling_stage, design_electrical_stage, design_flow_ratio, economic_schedule, npv, planned_return_temperature_c, required_cooling_mw, source_temperature_c, storage_heating_power_mw, variable_capex_eur
from run_all import coupled_npv, electrical_values_mw
from validation import run_validation, simulate_failure


class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with open("data/parameters.yml", encoding="utf-8") as handle:
            cls.p = yaml.safe_load(handle)

    def test_forecast_anchor(self) -> None:
        self.assertEqual(source_temperature_c(10.0, self.p), 100.0)

    def test_full_flow_load(self) -> None:
        self.assertAlmostEqual(float(required_cooling_mw(10.0, self.p)), 877.781145245, places=6)

    def test_cooling_split(self) -> None:
        stage = cooling_stage(10.0, self.p)
        self.assertAlmostEqual(stage.dry_mw + stage.chiller_mw, stage.total_mw, places=9)
        self.assertGreater(stage.dry_mw, stage.chiller_mw)

    def test_storage_is_lower_bound(self) -> None:
        self.assertLess(storage_heating_power_mw(self.p), float(required_cooling_mw(10.0, self.p)))

    def test_replacement_uses_engineering_multiplier(self) -> None:
        rows = economic_schedule(self.p, "hybrid")
        expected = self.p["plant"]["replacement_fraction"] * (1.0 + self.p["cost"]["engineering_contingency_fraction"]) * sum(variable_capex_eur(10.0, self.p).values())
        self.assertAlmostEqual(rows[self.p["plant"]["replacement_year"]]["replacement_eur"], expected, places=6)

    def test_return_ramp_and_backup_fuel(self) -> None:
        ramp = (self.p["ecology"]["ramp_stress_start_c"] - self.p["scenario"]["target_temperature_c"]) / self.p["ecology"]["maximum_return_rate_k_h"]
        self.assertEqual(ramp, 91.0)
        time_h = np.linspace(0.0, ramp + 1.0, 921)
        temperature = planned_return_temperature_c(time_h, self.p)
        self.assertEqual(temperature[-1], self.p["scenario"]["target_temperature_c"])
        self.assertLessEqual(float(np.max(np.abs(np.diff(temperature) / np.diff(time_h)))), 1.0 + 1e-12)
        expected_fuel = design_electrical_stage(self.p).electricity_mw * 1000.0 * self.p["plant"]["backup_duration_hours"] / (self.p["plant"]["backup_thermal_efficiency"] * self.p["plant"]["diesel_energy_kwh_l"])
        self.assertAlmostEqual(backup_fuel_liters(self.p), expected_fuel, places=6)
        self.assertGreater(backup_fuel_liters(self.p), 2e6)

    def test_design_capacity(self) -> None:
        ratio = self.p["hydrology"]["design_discharge_m3_s"] / self.p["water"]["discharge_m3_s"]
        design = cooling_stage(10.0, self.p, affected_fraction=ratio)
        installed = design.total_mw * (1.0 + self.p["plant"]["reserve_fraction"])
        self.assertAlmostEqual(design.total_mw, 999.702 * 4.7 * 4195.14 * 91.0 / 1e6, places=9)
        self.assertGreater(installed, design.total_mw)
        self.assertEqual(self.p["plant"]["module_count"], self.p["plant"]["required_modules"] + 1)
        self.assertEqual(variable_capex_eur(1.0, self.p)["backup_power"], variable_capex_eur(10.0, self.p)["backup_power"])

    def test_electrical_design_at_minimum_cop(self) -> None:
        stage = design_electrical_stage(self.p)
        self.assertAlmostEqual(stage.electricity_mw, 234.336, places=3)
        electricity, air_rejection = electrical_values_mw(self.p, self.p["hydrology"]["design_discharge_m3_s"], self.p["uncertainty"]["cop_low"])
        self.assertAlmostEqual(electricity, stage.electricity_mw, places=9)
        self.assertAlmostEqual(air_rejection, stage.air_rejection_mw, places=9)
        capacity = self.p["failure"]["backup_aggregate_capacity_mw"]
        required = int(np.ceil(stage.electricity_mw / capacity))
        self.assertEqual(required, 7)
        self.assertEqual(required + 1, 8)
        self.assertGreaterEqual(required * capacity, stage.electricity_mw)
        self.assertLess((required - 1) * capacity, stage.electricity_mw)

    def test_evaporative_pinch(self) -> None:
        stage = cooling_stage(10.0, self.p, technology="evaporative")
        hot_inlet = self.p["scenario"]["source_temperature_cap_c"]
        source_outlet = self.p["plant"]["evaporative_source_outlet_c"]
        secondary_inlet = self.p["plant"]["evaporative_secondary_inlet_c"]
        secondary_outlet = self.p["plant"]["evaporative_secondary_outlet_c"]
        self.assertAlmostEqual(hot_inlet - secondary_outlet, 4.0, places=9)
        self.assertAlmostEqual(source_outlet - secondary_inlet, 4.0, places=9)
        expected_dry = (hot_inlet - source_outlet) * self.p["water"]["density_kg_m3"] * self.p["water"]["discharge_m3_s"] * self.p["water"]["specific_heat_j_kgk"] / 1e6
        secondary_gain = (secondary_outlet - secondary_inlet) * self.p["water"]["density_kg_m3"] * self.p["plant"]["evaporative_secondary_flow_m3_s"] * self.p["water"]["specific_heat_j_kgk"] / 1e6
        self.assertAlmostEqual(stage.dry_mw, expected_dry, places=9)
        self.assertAlmostEqual(expected_dry, secondary_gain, places=9)

    def test_volume_sensitivity(self) -> None:
        low = copy.deepcopy(self.p)
        high = copy.deepcopy(self.p)
        low["scenario"]["pool_volume_m3"] = 10000.0
        high["scenario"]["pool_volume_m3"] = 50000.0
        low_failure = simulate_failure(low, design_flow_ratio(low), rtol=1e-11, atol=1e-11, max_step_s=5.0)
        high_failure = simulate_failure(high, design_flow_ratio(high), rtol=1e-11, atol=1e-11, max_step_s=5.0)
        self.assertLess(low_failure["recovery_margin_minutes"], high_failure["recovery_margin_minutes"])
        self.assertGreater(low_failure["recovery_peak_temperature_c"], high_failure["recovery_peak_temperature_c"])

    def test_coupled_npv_at_design_point(self) -> None:
        design_p = copy.deepcopy(self.p)
        design_p["water"]["discharge_m3_s"] = self.p["hydrology"]["design_discharge_m3_s"]
        actual = coupled_npv(self.p, self.p["hydrology"]["design_discharge_m3_s"], self.p["plant"]["chiller_cop"], 1.0)
        expected = npv(economic_schedule(design_p, "hybrid"))
        self.assertAlmostEqual(actual, expected, places=3)

    def test_guard_backup_scales_with_electricity(self) -> None:
        guard = copy.deepcopy(self.p)
        guard["scenario"]["target_temperature_c"] = self.p["hydrology"]["surface_saturation_c"] - self.p["hydrology"]["boiling_margin_k"]
        guard["hydrology"]["design_discharge_m3_s"] = guard["water"]["discharge_m3_s"]
        guard_electricity = design_electrical_stage(guard).electricity_mw
        reference_electricity = design_electrical_stage(self.p).electricity_mw
        expected = (self.p["cost"]["backup_power_eur"] + backup_fuel_cost_eur(self.p)) * guard_electricity / reference_electricity
        actual = variable_capex_eur(10.0, guard)["backup_power"]
        self.assertAlmostEqual(actual, expected, places=6)
        self.assertLess(actual, 1e6)

    def test_partial_flow_backup_and_capex(self) -> None:
        varied = copy.deepcopy(self.p)
        varied["scenario"]["affected_flow_fraction"] = 0.001
        backup = variable_capex_eur(10.0, varied)["backup_power"]
        rows = economic_schedule(varied, "hybrid")
        self.assertLess(backup, 1e6)
        self.assertLess(rows[10]["installed_capex_eur"], 10e6)
        varied["scenario"]["affected_flow_fraction"] = 0.01
        rows = economic_schedule(varied, "hybrid")
        self.assertLess(rows[10]["installed_capex_eur"], 30e6)

    def test_evaporative_backup_uses_evaporative_reference(self) -> None:
        design_electricity = design_electrical_stage(self.p, technology="evaporative").electricity_mw
        reference_electricity = design_electrical_stage(self.p, technology="evaporative").electricity_mw
        expected = (self.p["cost"]["backup_power_eur"] + backup_fuel_cost_eur(self.p, "evaporative")) * design_electricity / reference_electricity
        actual = variable_capex_eur(10.0, self.p, "evaporative")["backup_power"]
        self.assertAlmostEqual(actual, expected, places=6)

    def test_operating_year_count(self) -> None:
        rows = economic_schedule(self.p, "hybrid")
        self.assertEqual(len(rows), 26)
        self.assertEqual(rows[0]["maintenance_eur"], 0.0)
        self.assertEqual(rows[0]["net_operation_eur"], 0.0)
        self.assertEqual(rows[0]["electricity_mwh"], 0.0)
        self.assertEqual(sum(row["year"] > 0 and row["net_operation_eur"] > 0.0 for row in rows), 25)

    def test_evaporative_has_summer_chiller(self) -> None:
        stage = cooling_stage(10.0, self.p, technology="evaporative")
        self.assertGreater(stage.chiller_mw, 0.0)
        self.assertLess(stage.dry_mw, stage.total_mw)
        self.assertAlmostEqual(stage.air_rejection_mw, stage.total_mw + stage.electricity_mw, places=9)

    def test_backup_shortfall_increases_cost(self) -> None:
        varied = copy.deepcopy(self.p)
        varied["plant"]["availability"] = 0.95
        rows = economic_schedule(varied, "hybrid", backup_shortfall=True)
        self.assertGreater(npv(rows), npv(economic_schedule(self.p, "hybrid")))
        self.assertGreater(rows[10]["backup_fuel_liters"], 0.0)
        self.assertEqual(rows[10]["backup_cost_eur"], rows[10]["backup_fuel_liters"] * self.p["plant"]["diesel_price_eur_l"])

    def test_failure_p90_and_convergence(self) -> None:
        result = run_validation(self.p)
        failure = result["failure_p90"]
        self.assertEqual(failure["cooling_start_absolute_minutes"], 5.5)
        self.assertEqual(failure["full_cooling_absolute_minutes"], 10.5)
        self.assertAlmostEqual(failure["failure_time_to_20c_h"] * 60.0, 11.4213539, places=5)
        self.assertAlmostEqual(failure["recovery_margin_minutes"], 0.9213539, places=5)
        ratio = self.p["hydrology"]["design_discharge_m3_s"] / self.p["water"]["discharge_m3_s"]
        tau_seconds = self.p["scenario"]["pool_volume_m3"] / (self.p["water"]["discharge_m3_s"] * ratio)
        at_start = 100.0 - 91.0 * np.exp(-5.5 * 60.0 / tau_seconds)
        duration_seconds = 5.0 * 60.0
        cooling_k_s = required_cooling_mw(10.0, self.p, affected_fraction=ratio) * 1e6 / (self.p["water"]["density_kg_m3"] * self.p["scenario"]["pool_volume_m3"] * self.p["water"]["specific_heat_j_kgk"])
        integration_constant = 100.0 + tau_seconds ** 2 * cooling_k_s / duration_seconds
        particular_slope = -tau_seconds * cooling_k_s / duration_seconds
        peak_time_s = -tau_seconds * np.log(particular_slope * tau_seconds / (at_start - integration_constant))
        self.assertGreater(peak_time_s, 0.0)
        self.assertLess(peak_time_s, duration_seconds)
        at_peak = integration_constant + particular_slope * peak_time_s + (at_start - integration_constant) * np.exp(-peak_time_s / tau_seconds)
        self.assertAlmostEqual(failure["recovery_peak_temperature_c"], at_peak, places=5)
        self.assertLess(result["failure_p90_convergence_error_k"], 1e-6)

    def test_validation_suite(self) -> None:
        result = run_validation(self.p)
        self.assertTrue(result["all_checks_passed"])
        self.assertLess(result["recovery_peak_temperature_c"], 20.0)
        self.assertGreater(result["recovery_margin_minutes"], 0.0)


if __name__ == "__main__":
    unittest.main()
