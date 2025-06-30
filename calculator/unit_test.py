# test_unit.py
import unittest
from main import sub

class Testsubion(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sub(10, 5), 5)

    def test_negative_result(self):
        self.assertEqual(sub(5, 10), -5)

    def test_zero(self):
        self.assertEqual(sub(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
