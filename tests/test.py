"""
Usage:
    python -m unittest tests.test
With coverage:
    coverage run -m unittest tests.test
    coverage report
"""

import unittest

from py import calcs


class Levenshtein(unittest.TestCase):
    def test(self):
        """
        Tests for calcs.levenshtein.
        """
        sample = [
            [None, None, 0],
            [None, '', None],
            ['', None, None],
            ['', '', 0],
            ['xx', '', 2],
            ['', 'xx', 2],
            ['XX', 'Xy', 1],
            ['xx', 'Xy', 2],
            ['xx', 'xy', 1],
            ['xx', 'xyz', 2],
            ['Alabama', 'Alaska', 3],
        ]
        for s1, s2, expected in sample:
            if expected is None:  # indicates that we expect an error
                with self.assertRaises(TypeError):
                    calcs.levenshtein(s1, s2)
            else:
                distance = calcs.levenshtein(s1, s2)
                self.assertEqual(distance, expected)
