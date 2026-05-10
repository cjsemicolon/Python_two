import unittest
from arithmatic_app import (
    generate_question,
    check_answer,
    calculate_score
)


class TestFunctions(unittest.TestCase):

    def test_generate_question_no_negative(self):
        first, second = generate_question()
        self.assertGreaterEqual(first, second)

    def test_check_answer_correct(self):
        self.assertTrue(check_answer(10, 5, 5))

    def test_check_answer_incorrect(self):
        self.assertFalse(check_answer(10, 5, 3))

    def test_calculate_score(self):
        self.assertEqual(calculate_score(8, 10), 80.0)

    def test_calculate_score_zero(self):
        self.assertEqual(calculate_score(0, 10), 0.0)

