import json
import os
import sys
from pathlib import Path

from octane11 import history, requests

sys.path.append(os.path.join(Path(__file__).resolve().parent))

import pytest


@pytest.fixture()
def history_api_response():
    class Response:
        def json(self):
            return {
                "amount": 1.0,
                "base": "USD",
                "start_date": "2021-02-01",
                "end_date": "2021-02-02",
                "rates": {
                    "2021-02-01": {
                        "CAD": 1.2805,
                        "EUR": 0.82754
                    },
                    "2021-02-02": {
                        "CAD": 1.2805,
                        "EUR": 0.83029
                    }
                }
            }
    return Response()

def test_history(history_api_response, monkeypatch):
    monkeypatch.setattr(requests, "get", lambda url, params: history_api_response)

    start = "2021-02-01"
    end = "2021-02-02"
    base = "USD"
    symbol = ["EUR", "CAD"]
    result = history(start, end, base, symbol, "")
    result_0 = json.loads(result[0])
    result_3 = json.loads(result[3])

    assert len(result) == 4
    assert result_0["date"] == "2021-02-01"
    assert result_3["date"] == "2021-02-02"
    assert result_0["base"] == "USD"
    assert result_3["base"] == "USD"
    assert result_0["symbol"] == "CAD"
    assert result_3["symbol"] == "EUR"
    assert result_0["rate"] == 1.2805
    assert result_3["rate"] == 0.83029
