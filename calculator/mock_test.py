# test_mock.py
import unittest
from unittest.mock import Mock
from main import sub

class TestSubtractionWithMock(unittest.TestCase):
    def test_subtract_with_mock(self):
        fake_data = Mock()
        fake_data.get_value.return_value = 20

        result = sub(fake_data.get_value(), 5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
