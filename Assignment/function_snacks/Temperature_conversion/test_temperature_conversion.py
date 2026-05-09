import unittest
from temperature_conversion import temperature_conversion


class TestTemperatureAdvisory(unittest.TestCase):

    def test_celsius_conversion_heat(self):
        self.assertEqual(
            temperature_conversion(40, 100, 'C'),
            "Heat alert"
        )

    def test_celsius_conversion_cold(self):
        self.assertEqual(
            temperature_conversion(20, 100, 'C'),
            "Cold advisory"
        )

    def test_fahrenheit_conversion_heat(self):
        self.assertEqual(
            temperature_conversion(212, 50, 'F'),
            "Heat alert"
        )

    def test_fahrenheit_conversion_cold(self):
        self.assertEqual(
            temperature_conversion(32, 10, 'F'),
            "Cold advisory"
        )

    def test_default_unit(self):
        self.assertEqual(
            temperature_conversion(30, 80),
            "Heat alert"
        )

    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            temperature_conversion(30, 80, 'K')


