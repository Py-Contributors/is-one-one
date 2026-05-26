"""Test suite for is_one_one — now with proper unittest structure."""

import unittest
import is_one_one
import sys
import io

# Fix for Windows console encoding issues with emojis
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class TestIsOne(unittest.TestCase):
    """Verify that 1 is indeed 1, across all dimensions and realities."""

    def test_is_one(self):
        """The only normal check in this entire repo."""
        self.assertTrue(is_one_one.is_one())

    def test_is_one_unicode_distance(self):
        """Distance between 'a' and 'b' is 1."""
        self.assertTrue(is_one_one.is_one_unicode_distance())

    def test_is_one_using_time_travel(self):
        """Time travel confirms 1 == 1."""
        self.assertTrue(is_one_one.is_one_using_time_travel())

    def test_is_one_using_interdimensional_tax_fraud(self):
        """Interdimensional tax fraud also confirms 1 == 1."""
        self.assertTrue(is_one_one.is_one_using_interdimensional_tax_fraud())

    def test_is_one_using_binary(self):
        """Binary decoding proves 1 is 1."""
        self.assertTrue(is_one_one.is_one_using_binary())

    def test_is_one_under_extreme_pressure(self):
        """50 layers of dictionaries cannot hide the truth."""
        self.assertTrue(is_one_one.is_one_under_extreme_pressure())

    def test_is_one_using_roman_numerals(self):
        """Roman numeral I equals 1."""
        self.assertTrue(is_one_one.is_one_using_roman_numerals())

    def test_the_one_suriya(self):
        """Verify that Suriya is number one."""
        self.assertTrue(is_one_one.the_one_suriya())

    def test_is_one_using_vector_magnitude(self):
        """The magnitude of a unit vector is one."""
        self.assertTrue(is_one_one.is_one_using_vector_magnitude())

    def test_is_one_using_existential_crisis(self):
        """A full philosophical breakdown confirms 1 == 1."""
        self.assertTrue(is_one_one.is_one_using_existential_crisis())

    def test_is_one_just_to_be_sure(self):
        """The ultimate recursive confirmation."""
        self.assertTrue(is_one_one.is_one_just_to_be_sure())


class TestIsNumberOne(unittest.TestCase):
    """Negative testing — verify is_number_one rejects non-one values."""

    def test_one_is_one(self):
        """1 should be recognized as 1."""
        self.assertTrue(is_one_one.is_number_one(1))

    def test_two_is_not_one(self):
        """2 is not 1 — the first function in this repo that can return False."""
        self.assertFalse(is_one_one.is_number_one(2))

    def test_zero_is_not_one(self):
        """0 is not 1."""
        self.assertFalse(is_one_one.is_number_one(0))

    def test_negative_one_is_not_one(self):
        """-1 is not 1 (even though it contains '1')."""
        self.assertFalse(is_one_one.is_number_one(-1))

    def test_large_number_is_not_one(self):
        """9999 is definitely not 1."""
        self.assertFalse(is_one_one.is_number_one(9999))


if __name__ == "__main__":
    unittest.main()
