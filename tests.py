"""
Usage:
    python -m unittest tests
With coverage:
    coverage run -m unittest tests
    coverage report
"""

import unittest

from levenshtein import levenshtein


class Levenshtein(unittest.TestCase):
    def test_values(self):
        """
        Tests for levenshtein.
        """
        values = [
            ['Nebraska', 'Bill Brasky', 7],
            ['aa', '', 2],
            ['', 'aa', 2],
            ['AA', 'Aa', 1],
            ['ab', 'Aa', 2],
            ['aa', 'ab', 1],
            ['a', 'abc', 2],
        ]
        for a, b, expected in values:
            distance = levenshtein(a, b)
            self.assertEqual(distance, expected)

    def test_blank(self):
        self.assertEquals(levenshtein('', ''), 0)

    def test_nulls(self):
        values = [
            [None, "word"],
            ["word", None],
            [None, None]
        ]
        for a, b in values:
            # two values are required to compute the edit distance
            self.assertRaises(TypeError)
