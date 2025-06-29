# app/api_call.py
import requests

def get_subtraction(a, b):
    response = requests.get(f"http://example.com/api/subtract?a={a}&b={b}")
    return response.json()['result']
