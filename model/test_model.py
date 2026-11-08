from __future__ import annotations

import copy
import unittest

import yaml

import numpy as np

from core import backup_fuel_cost_eur, backup_fuel_liters, cooling_stage, design_flow_ratio, economic_schedule, npv, planned_return_temperature_c, required_cooling_mw, source_temperature_c, storage_heating_power_mw, variable_capex_eur
from run_all import coupled_npv
from validation import run_validation


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
        design_ratio = self.p["hydrology"]["design_discharge_m3_s"] / self.p["water"]["discharge_m3_s"]
        expected_fuel = cooling_stage(10.0, self.p, affected_fraction=design_ratio).electricity_mw * 1000.0 * self.p["plant"]["backup_duration_hours"] / (self.p["plant"]["backup_thermal_efficiency"] * self.p["plant"]["diesel_energy_kwh_l"])
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
        guard_electricity = cooling_stage(10.0, guard).electricity_mw
        reference_electricity = cooling_stage(10.0, self.p, affected_fraction=design_flow_ratio(self.p)).electricity_mw
        expected = (self.p["cost"]["backup_power_eur"] + backup_fuel_cost_eur(self.p)) * guard_electricity / reference_electricity
        actual = variable_capex_eur(10.0, guard)["backup_power"]
        self.assertAlmostEqual(actual, expected, places=6)
        self.assertLess(actual, 1e6)

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
