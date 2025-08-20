import unittest
from app.utils import add, validate_integrity, break_into_digits, bulk_filter

class TestUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, add(1,2))

    def test_integrity_validator(self):
        self.assertFalse(validate_integrity(0))
        self.assertTrue(validate_integrity(1))
        self.assertFalse(validate_integrity(-12))
        self.assertTrue(validate_integrity(18))
        self.assertFalse(validate_integrity(19))

    def test_break_into_digits(self):
        self.assertListEqual([1, 2, 3], break_into_digits(123))

    def test_bulk_filter(self):
        self.assertListEqual([1, 2, 3], list(bulk_filter(3)))
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20], list(bulk_filter(20)))

if __name__ == "__main__":
    unittest.main()
