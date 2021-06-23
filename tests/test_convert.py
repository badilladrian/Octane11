"""Test cases for convert command"""
import os
import sys
from pathlib import Path
import pytest

from octane11 import convert, requests

sys.path.append(os.path.join(Path(__file__).resolve().parent))



@pytest.fixture()
def convert_api_response():
    """Mock object for request responses"""
    class Response:
        def json(self):
            return {"amount": 50.0, "base": "USD", "date": "2021-02-01", "rates": {"EUR": 41.377}}

    return Response()


def test_convert(convert_api_response, monkeypatch):
    """sucessful scenario for convert command"""
    monkeypatch.setattr(requests, "get", lambda url, params: convert_api_response)

    date = "2021-02-01"
    base = "USD"
    symbol = "EUR"
    amount = 50
    result = convert(date, base, symbol, amount)

    assert result == 41.377
