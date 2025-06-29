# tests/test_subtract_functional.py
import unittest
from app.routes import app  # ✅ correct way to import the Flask app

class TestSubtractionFunctional(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_subtract(self):
        res = self.client.get('/subtract?a=10&b=4')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['result'], 6)
