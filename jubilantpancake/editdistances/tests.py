"""
Unit tests
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from editdistances.views import home


class HomeTest(TestCase):
    """
    Class of unit tests for home page
    """

    def test_root_resolves_home(self):
        """
        root uses home
        """
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_successful_request(self):
        """
        tests connection
        """
        request = HttpRequest()
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_home_edit_dist_on_post(self):
        """
        returns json of edit distance of different
        words after receiving post of 2 input items
        """
        request = HttpRequest()
        request.method = 'POST'
        request.POST['input_1'] = 'kitten'
        request.POST['input_2'] = 'sitting'

        response = home(request)
        content = response.content
        self.assertEqual(content, b'{"edit_distance": 3}')

        request = HttpRequest()
        request.method = 'POST'
        request.POST['input_1'] = 'kitten'
        request.POST['input_2'] = 'kitten'

        response = home(request)
        content = response.content
        self.assertEqual(content, b'{"edit_distance": 0}')
