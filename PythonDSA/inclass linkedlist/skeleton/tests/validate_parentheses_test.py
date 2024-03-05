import unittest

from src.tasks import validate_parentheses

class ValidateParentheses_Tests(unittest.TestCase):
    def test_one(self):
        self.assertTrue(validate_parentheses('(1 + (2 * 3))'))

    def test_two(self):
        self.assertFalse(validate_parentheses('1 + (2 * 3))'))

    def test_three(self):
        self.assertFalse(validate_parentheses('(1 + )2 * 3))'))

    def test_four(self):
        self.assertFalse(validate_parentheses('(1 + (2 * 3)'))

    def test_five(self):
        self.assertTrue(validate_parentheses('((((5 / 2) + 8) - 1 ) * 3) + 12'))

    def test_six(self):
        self.assertFalse(validate_parentheses(')12 + 3 + (2 * 8)'))
