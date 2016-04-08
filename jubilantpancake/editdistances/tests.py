from django.test import TestCase


class SmokeTest(TestCase):

    def test_bad_string_match(self):
        self.assertEqual('monty', 'python')
