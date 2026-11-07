from __future__ import annotations

import unittest

import yaml

from core import cooling_stage, required_cooling_mw, source_temperature_c, storage_heating_power_mw
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

    def test_validation_suite(self) -> None:
        self.assertTrue(run_validation(self.p)["all_checks_passed"])


if __name__ == "__main__":
    unittest.main()
