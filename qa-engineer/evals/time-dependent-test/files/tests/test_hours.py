import unittest

from app.hours import greeting


class HoursTests(unittest.TestCase):
    def test_open_greeting(self):
        self.assertEqual(greeting(), "We are open")
