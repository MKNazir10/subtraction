import unittest
from app.logic import subtract

class TestSubtractionUnit(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -2), -3)

    def test_mix_positive_negative(self):
        self.assertEqual(subtract(5, -2), 7)

    def test_zero_case(self):
        self.assertEqual(subtract(0, 5), -5)

    def test_same_number(self):
        self.assertEqual(subtract(3, 3), 0)

if __name__ == '__main__':
    unittest.main()
