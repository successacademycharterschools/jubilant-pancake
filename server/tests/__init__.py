import unittest

from .. import application


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        application.app.config['TESTING'] = True
        self.app = application.app.test_client()

    def test_index_success(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
