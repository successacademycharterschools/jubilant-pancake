# -*- coding: utf-8 -*-
# Python
from unittest import main, TestCase

# External
from distance import levenshtein

class EditDistanceTestCase(TestCase):
    """Tests for the edit distance library"""

    def test_none_word(self):
        with self.assertRaises(TypeError):
            edit_distance = levenshtein('word', None)

    def test_int_word(self):
        with self.assertRaises(TypeError):
            edit_distance = levenshtein('word', 0)

    def test_blank_words(self):
        edit_distance = levenshtein('', '')
        self.assertEqual(edit_distance, 0)

    def test_unicode_words(self):
        edit_distance = levenshtein('', '人')
        self.assertEqual(edit_distance, 1)

    def test_diff_one(self):
        edit_distance = levenshtein('', 'a')
        self.assertEqual(edit_distance, 1)

    def test_diff_two(self):
        edit_distance = levenshtein('aa', 'bb')
        self.assertEqual(edit_distance, 2)

    def test_diff_three(self):
        edit_distance = levenshtein('abcabcabc', 'abdabdabd')
        self.assertEqual(edit_distance, 3)

if __name__ == '__main__':
    main()
