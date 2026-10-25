import os
import unittest

from app.rates import fetch_rate


@unittest.skipUnless(os.environ.get("RATES_LIVE") == "1", "live test; set RATES_LIVE=1 and start stub/rates_server.py")
class LiveRatesTests(unittest.TestCase):
    def test_fetch_rate_matches_service(self):
        self.assertEqual(fetch_rate("EUR"), 2.0)
