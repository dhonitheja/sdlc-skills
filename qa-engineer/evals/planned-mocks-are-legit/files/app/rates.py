import json
import urllib.request


def fetch_rate(currency):
    with urllib.request.urlopen(f"https://rates.example.invalid/v1/{currency}", timeout=5) as r:
        return float(json.load(r)["rate"])
