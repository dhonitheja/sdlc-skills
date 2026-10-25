import json
import urllib.request

# Placeholder host: replace with the real vendor endpoint before using this outside tests.
RATES_BASE_URL = "https://rates.example.invalid/v1"


def fetch_rate(currency):
    with urllib.request.urlopen(f"{RATES_BASE_URL}/{currency}", timeout=5) as r:
        return float(json.load(r)["rate"])
