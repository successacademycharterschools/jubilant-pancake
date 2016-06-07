import unittest
import json

from .. import application


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        application.app.config['TESTING'] = True
        self.app = application.app.test_client()

    def test_index_success(self):
        '''
        Make sure that our index page loads without errors
        '''
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)

    def _med_case_factory(self, input_data, expected_steps):
        '''
        A utility for taking a dict for converstion to a JSON string to be
        submitted as the POST body to the minimum edit distance API endpoint
        '''
        input_data = json.dumps(input_data)

        resp = self.app.post('/api/edit-distance/', data=input_data)

        self.assertEqual(resp.status_code, 200)

        output_data = json.loads(resp.data)

        self.assertEqual(output_data.get('steps'), expected_steps)

    def test_identical_med(self):
        '''
        Make sure that identical strings return 0 MED
        '''
        input_data = {
            'str1': 'abc',
            'str2': 'abc',
        }
        self._med_case_factory(input_data, 0)

    def test_simple_insertion_med(self):
        '''
        Make sure that we properly compute simple insertion for MED
        '''
        input_data = {
            'str1': 'abc',
            'str2': 'abcd',
        }
        self._med_case_factory(input_data, 1)

    def test_simple_deletion_med(self):
        '''
        Make sure that we properly compute simple deletion for MED
        '''
        input_data = {
            'str1': 'abc',
            'str2': 'ab',
        }
        self._med_case_factory(input_data, 1)

    def test_simple_substitution_med(self):
        '''
        Make sure that we properly compute simple substitution for MED
        '''
        input_data = {
            'str1': 'abc',
            'str2': 'ab2',
        }
        self._med_case_factory(input_data, 2)

    def test_complex_substitution_med(self):
        '''
        Make sure that we properly compute a more complex "real world" test
        case
        '''
        input_data = {
            'str1': 'polygonal',
            'str2': 'polymorphous',
        }
        self._med_case_factory(input_data, 11)

    def test_missing_value_med(self):
        '''
        Make sure that we compute missing inputs as empty strings
        '''
        input_data = {
            'str1': 'abc',
        }
        self._med_case_factory(input_data, 3)
