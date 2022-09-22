import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1, 1, 1, 0.9]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0, 0.1, 0.2, 0.7]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())