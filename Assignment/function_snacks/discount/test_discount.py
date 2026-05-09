import unittest
from discount import apply_discount


class TestApplyDiscount(unittest.TestCase):

    def test_save10_discount(self):
        self.assertEqual(
            apply_discount("Bag", 100, "SAVE10"),
            90.0
        )

    def test_halfoff_discount(self):
        self.assertEqual(
            apply_discount("Phone", 200, "HALFOFF"),
            100.0
        )

    def test_invalid_code(self):
        self.assertEqual(
            apply_discount("Book", 50, "INVALID"),
            50
        )

    def test_lowercase_code(self):
        self.assertEqual(
            apply_discount("Shoes", 100, "save10"),
            90.0
        )

    def test_zero_price(self):
        self.assertEqual(
            apply_discount("Pen", 0, "SAVE10"),
            0
        )

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            apply_discount("Laptop", -500, "SAVE10")


