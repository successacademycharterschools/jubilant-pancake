import unittest
import distance

class TestCase(unittest.TestCase):
    def test_check_equal(self):
        ingredient1 = "cake"
        ingredient2 = "cake"
        assert distance.levenshtein(ingredient1, ingredient2) == 0
    def test_check_diff_1(self):
        ingredient1 = "blueberries"
        ingredient2 = "strawberries"
        assert distance.levenshtein(ingredient1, ingredient2) == 5
    def test_check_diff_2(self):
        ingredient1 = ""
        ingredient2 = "bananas" 
        assert distance.levenshtein(ingredient1, ingredient2) == 7

if __name__ == "__main__":
    unittest.main()

