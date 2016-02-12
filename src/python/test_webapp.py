#!/usr/bin/env python2.7

import unittest

from webob import Request
from webob import Response

from webapp import StringComparitorApp


class TestStringComparitor(unittest.TestCase):

    def test_get(self):
        app = StringComparitorApp()
        req = Request.blank('')
        response = app(req)

    def test_post(self):
        app = StringComparitorApp()
        req = Request.blank('/compare')
        req.method = 'POST'
        response = app(req)

    def test_put(self):
        app = StringComparitorApp()
        req = Request.blank('')
        req.method = 'PUT'
        response = app(req)
        self.assertEqual(500, response.status_code)


if __name__ == "__main__":
    unittest.main()
