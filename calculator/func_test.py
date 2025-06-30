# test_functional.py
import unittest
from main import sub

class TestSubtractionFunctional(unittest.TestCase):
    def test_subtraction_flow(self):
        inputs = [(100, 50), (0, 0), (3, 7)]
        expected_outputs = [50, 0, -4]

        for (a, b), expected in zip(inputs, expected_outputs):
            with self.subTest(a=a, b=b):
                self.assertEqual(sub(a, b), expected)

if __name__ == '__main__':
    unittest.main()