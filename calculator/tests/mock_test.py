import unittest
from unittest.mock import patch
from app.api_call import get_subtraction

class TestSubtractionAPIMock(unittest.TestCase):
    @patch('app.api_call.requests.get')
    def test_mock_api_response(self, mock_get):
        mock_get.return_value.json.return_value = {'result': 5}
        result = get_subtraction(10, 5)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
