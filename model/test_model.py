from __future__ import annotations

import unittest

import yaml

import numpy as np

from core import backup_fuel_liters, cooling_stage, economic_schedule, planned_return_temperature_c, required_cooling_mw, source_temperature_c, storage_heating_power_mw, variable_capex_eur
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
        expected_fuel = cooling_stage(10.0, self.p).electricity_mw * 1000.0 * self.p["plant"]["backup_duration_hours"] / (self.p["plant"]["backup_thermal_efficiency"] * self.p["plant"]["diesel_energy_kwh_l"])
        self.assertAlmostEqual(backup_fuel_liters(self.p), expected_fuel, places=6)
        self.assertAlmostEqual(backup_fuel_liters(self.p), 908657.1869030809, places=6)

    def test_validation_suite(self) -> None:
        self.assertTrue(run_validation(self.p)["all_checks_passed"])


if __name__ == "__main__":
    unittest.main()
