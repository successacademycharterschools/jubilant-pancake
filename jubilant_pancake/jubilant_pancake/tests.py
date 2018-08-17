"""Tests for Jubilant Pancake project"""
from json import dumps

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from .utils import wagner_fisher


class UtilsTestCase(TestCase):
    """Test for Jubilant Pancake utils"""

    def test_wagner_fisher(self):
        """This uses a known test case to show that wagner_fisher works"""
        string_1 = 'jubilant'
        string_2 = 'pancake'
        self.assertEqual(wagner_fisher(string_1, string_2), 7)


class ViewsTestCase(TestCase):
    """Tests for Jubilant Pancake views"""

    def test_pancake_view(self):
        """Test for main view"""
        client = Client()
        response = client.get(reverse('pancake'))
        self.assertContains(response, 'Enter your strings')

    def test_calculate_view(self):
        """Test for calculate view"""
        client = Client()
        data = {'string_1': 'jubilant', 'string_2': 'pancake'}
        response = client.post(
            reverse('calculate'), data=data)
        self.assertContains(response, dumps({'edit_distance': 7}))
