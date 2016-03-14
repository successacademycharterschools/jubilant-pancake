import unittest
from jubilant import levenshtein

class PrimesTestCase(unittest.TestCase):
    """Tests for levenshtein function"""

    def test_one_string_is_empty(self):
        """If one of two strings is empty, return len of non-empty string"""
        self.assertTrue(levenshtein("", "notempty")) == len("notempty")

    def test_string1_is_longer(self):
        """If first string is longer, check index stays in range"""
        self.assertTrue(levenshtein("notempty", "one")) == 6

    def test_string2_is_longer(self):
        """If second string is longer, check index stays in range"""
        self.assertTrue(levenshtein("one", "notempty")) == 6

    # test for some specific known good cases

    def test_Sunday_Monday(self):
        """string1 = Sunday; string2 = Monday"""
        self.assertTrue(levenshtein("Sunday", "Monday")) == 2

    def test_jubilant_pancake(self):
        """string1 = jubilant; string2 = pancake"""
        self.assertTrue(levenshtein("jubilant", "pancake")) == 7


if __name__ == '__main__':
    unittest.main()
