from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from editdistances.views import home


class HomeTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.status_code, 200)

    def test_home_page_calculates_edit_dist_on_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['input_1'] = 'kitten'
        request.POST['input_2'] = 'sitting'

        response = home(request)
        content = response.content
        self.assertEqual(content, b'{"edit_distance": 3}')

    def test_home_page_calculates_exact_strings(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['input_1'] = 'kitten'
        request.POST['input_2'] = 'kitten'

        response = home(request)
        content = response.content
        self.assertEqual(content, b'{"edit_distance": 0}')
