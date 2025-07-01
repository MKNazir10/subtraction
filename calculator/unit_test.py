"""Unit tests for the subtraction function in main.py"""

import unittest
from main import sub  # assuming main.py has a 'sub' function


class TestSubtraction(unittest.TestCase):
    """Test cases for the sub function"""

    def test_positive_numbers(self):
        """Test subtracting two positive numbers"""
        self.assertEqual(sub(10, 5), 5)

    def test_negative_result(self):
        """Test result when second number is larger"""
        self.assertEqual(sub(5, 10), -5)

    def test_zero(self):
        """Test subtracting zero from zero"""
        self.assertEqual(sub(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
