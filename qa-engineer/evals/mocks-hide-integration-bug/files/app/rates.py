import json
import os
import urllib.request

RATES_BASE_URL = os.environ.get("RATES_BASE_URL", "http://127.0.0.1:8201/v1")


def fetch_rate(currency):
    with urllib.request.urlopen(f"{RATES_BASE_URL}/{currency}", timeout=5) as r:
        return float(json.load(r)["rate"])
