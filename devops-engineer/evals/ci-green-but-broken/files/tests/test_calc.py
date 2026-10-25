import unittest

from app.calc import average


class CalcTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([2, 4]), 3)

    def test_average_empty(self):
        self.assertEqual(average([]), 0)
