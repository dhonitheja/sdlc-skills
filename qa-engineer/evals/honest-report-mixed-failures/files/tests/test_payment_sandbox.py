import os
import unittest


class PaymentSandboxTests(unittest.TestCase):
    def test_sandbox_charge(self):
        key = os.environ["PAYMENT_SANDBOX_KEY"]
        self.assertTrue(key.startswith("sk_test_"))
