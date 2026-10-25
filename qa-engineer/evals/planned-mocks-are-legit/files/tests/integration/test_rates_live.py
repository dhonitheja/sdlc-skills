import os
import unittest

from app.rates import fetch_rate


@unittest.skipUnless(os.environ.get("RATES_LIVE") == "1", "live API test; set RATES_LIVE=1")
class LiveRatesTests(unittest.TestCase):
    def test_fetch_rate_returns_number(self):
        self.assertIsInstance(fetch_rate("EUR"), float)
