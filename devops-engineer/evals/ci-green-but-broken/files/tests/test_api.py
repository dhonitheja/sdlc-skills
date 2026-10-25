import unittest

from app.api import auth_header


class ApiTests(unittest.TestCase):
    def test_header_has_bearer(self):
        self.assertTrue(auth_header()["Authorization"].startswith("Bearer "))
