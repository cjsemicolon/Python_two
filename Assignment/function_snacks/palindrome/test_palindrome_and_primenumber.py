import unittest
from palindrome_and_primenumber import palindrome_prime


class TestPalindromePrime(unittest.TestCase):

    def test_palindrome_prime_true(self):
        self.assertTrue(palindrome_prime(131))

    def test_not_prime(self):
        self.assertFalse(palindrome_prime(121))

    def test_not_palindrome(self):
        self.assertFalse(palindrome_prime(23))

    def test_single_digit_prime(self):
        self.assertTrue(palindrome_prime(7))

    def test_negative_number(self):
        self.assertFalse(palindrome_prime(-131))

    def test_zero(self):
        self.assertFalse(palindrome_prime(0))

    def test_one(self):
        self.assertFalse(palindrome_prime(1))



