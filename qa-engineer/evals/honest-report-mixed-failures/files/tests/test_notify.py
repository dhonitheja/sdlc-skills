import unittest
from app.notify import send


class NotifyTests(unittest.TestCase):
    def test_send_is_callable(self):
        self.assertTrue(callable(send))
