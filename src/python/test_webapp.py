#!/usr/bin/env python2.7

import ConfigParser
import json
import unittest

from webob import Request
from webob import Response

from webapp import StringComparitorApp


class TestStringComparitor(unittest.TestCase):

    def setUp(self):
        super(TestStringComparitor, self).setUp()
        self.app_config = ConfigParser.SafeConfigParser()
        with open("defaults.cfg", "r") as config_defaults:
            self.app_config.readfp(config_defaults)

    def tearDown(self):
        del self.app_config
        super(TestStringComparitor, self).tearDown()

    def test_get(self):
        app = StringComparitorApp(self.app_config)
        req = Request.blank('')
        response = app(req)
        self.assertNotEqual('', response.body)

    def test_post(self):
        app = StringComparitorApp(self.app_config)
        req = Request.blank('/compare')
        req.method = 'POST'
        args = {
            "source": "kitten",
            "target": "sitting",
        }
        req.body = json.dumps(args)
        response = app(req)
        edit_distance = json.loads(response.body)["edit_distance"]
        self.assertEqual(3, edit_distance)

    def test_put(self):
        app = StringComparitorApp(self.app_config)
        req = Request.blank('')
        req.method = 'PUT'
        response = app(req)
        self.assertEqual(500, response.status_code)


if __name__ == "__main__":
    unittest.main()
