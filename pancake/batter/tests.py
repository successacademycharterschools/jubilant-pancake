from django.test import TestCase
from pancake.batter.views import compute_distances


class ComputeTestCase(TestCase):
    def setUp(self):
        self.stringone = 'this is string one'
        self.stringtwo = 'string two this is'
        self.astring = 'aaaaa'
        self.bstring = 'bbbbb'
        self.thestring = 'the string'
        self.samestring = 'the string'
        self.emptystring = ''
        self.nostring = None


    def test_compute_distances(self):
        one_two_differences = compute_distances(self.stringone, self.stringtwo)
        ab_differences = compute_distances(self.astring, self.bstring)
        no_differences = compute_distances(self.thestring, self.samestring)
        empty_differences = compute_distances(self.thestring, self.emptystring)
        none_string_differences = compute_distances(self.thestring, self.nostring)

        self.assertEqual(one_two_differences['spaced'], 4)
        self.assertEqual(one_two_differences['full'], 14)
        self.assertEqual(one_two_differences['lcs'], set(['this is', 'string ']))
        self.assertEqual(one_two_differences['words_in_common'], 3)

        self.assertEqual(ab_differences['spaced'], 1)
        self.assertEqual(ab_differences['full'], 5)
        self.assertEqual(ab_differences['lcs'], set([]))
        self.assertEqual(ab_differences['words_in_common'], 0)

        self.assertEqual(no_differences['spaced'], 0)
        self.assertEqual(no_differences['full'], 0)
        self.assertEqual(no_differences['lcs'], set(['the string']))
        self.assertEqual(no_differences['words_in_common'], 2)

        self.assertEqual(empty_differences['spaced'], 2)
        self.assertEqual(empty_differences['full'], 10)
        self.assertEqual(empty_differences['lcs'], set([]))
        self.assertEqual(empty_differences['words_in_common'], 0)

        self.assertEqual(none_string_differences['spaced'], 2)
        self.assertEqual(none_string_differences['full'], 10)
        self.assertEqual(none_string_differences['lcs'], set([]))
        self.assertEqual(none_string_differences['words_in_common'], 0)



