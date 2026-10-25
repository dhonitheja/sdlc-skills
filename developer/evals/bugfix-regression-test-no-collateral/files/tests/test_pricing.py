import unittest

from app.pricing import bulk_discount, checkout_total, free_shipping


class PricingTests(unittest.TestCase):
    def test_no_discount_small_order(self):
        self.assertEqual(bulk_discount(100.0, 3), 100.0)

    def test_discount_large_order(self):
        self.assertEqual(bulk_discount(100.0, 12), 90.0)

    def test_free_shipping_over_ten(self):
        self.assertTrue(free_shipping(11))
        self.assertFalse(free_shipping(10))

    def test_checkout_total_small(self):
        self.assertEqual(checkout_total([(10.0, 2)], 0.1), 22.0)
