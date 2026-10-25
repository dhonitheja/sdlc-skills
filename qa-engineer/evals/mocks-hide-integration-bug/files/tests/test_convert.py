import unittest
from unittest.mock import patch

from app.convert import convert


class ConvertTests(unittest.TestCase):
    @patch("app.rates.fetch_rate", return_value=2.0)
    def test_converts_using_rate(self, _):
        self.assertEqual(convert(10, "EUR"), 20.0)

    @patch("app.rates.fetch_rate", return_value=0.333)
    def test_rounds_to_cents(self, _):
        self.assertEqual(convert(10, "EUR"), 3.33)

    @patch("app.rates.fetch_rate", return_value=1.5)
    def test_zero_amount(self, _):
        self.assertEqual(convert(0, "EUR"), 0.0)
