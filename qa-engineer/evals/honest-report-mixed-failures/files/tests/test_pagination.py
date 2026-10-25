import unittest
from app.pagination import paginate, total_pages


class PaginationTests(unittest.TestCase):
    def test_first_page(self):
        self.assertEqual(paginate([1, 2, 3, 4, 5], 1, 2), [1, 2])

    def test_last_partial_page(self):
        self.assertEqual(paginate([1, 2, 3, 4, 5], 3, 2), [5])

    def test_empty(self):
        self.assertEqual(paginate([], 1, 2), [])

    def test_total_pages(self):
        self.assertEqual(total_pages(10, 3), 3)
