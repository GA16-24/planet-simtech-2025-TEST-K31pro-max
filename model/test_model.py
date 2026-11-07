from __future__ import annotations

import copy
import unittest

import yaml

import numpy as np

from core import backup_fuel_liters, cooling_stage, economic_schedule, npv, planned_return_temperature_c, required_cooling_mw, source_temperature_c, storage_heating_power_mw, variable_capex_eur
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
        self.assertAlmostEqual(result["failure_mean"]["recovery_peak_temperature_c"], 12.6447637, places=5)
        self.assertAlmostEqual(result["failure_p90"]["recovery_peak_temperature_c"], 16.2044656, places=4)
        self.assertAlmostEqual(result["failure_p90"]["failure_time_to_20c_h"] * 60.0, 11.4213539, places=5)
        self.assertAlmostEqual(result["failure_p90"]["recovery_margin_minutes"], 1.4213539, places=5)
        self.assertLess(result["failure_p90_convergence_error_k"], 1e-6)

    def test_validation_suite(self) -> None:
        result = run_validation(self.p)
        self.assertTrue(result["all_checks_passed"])
        self.assertLess(result["recovery_peak_temperature_c"], 20.0)
        self.assertGreater(result["recovery_margin_minutes"], 0.0)


if __name__ == "__main__":
    unittest.main()
