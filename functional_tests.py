"""
Functional test or end-to-end tests.
These simulate how a user would interact with the application.
"""
import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    """
    Class of user interactions, simulated test, setup and breakdown
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_submit_form_returns_dist(self):
        """
        Simulates user interactions with application
        """
        # User goes to Jubilant Pancake homepage
        self.browser.get('http://localhost:8000')

        # User sees page title
        self.assertIn('Jubilant Pancake', self.browser.title)

        # User sees a paragraph about the site
        description_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('edit distance', description_text)

        # User sees 2 text input fields and a centered placeholder
        input_1 = self.browser.find_element_by_id('input_1')
        input_2 = self.browser.find_element_by_id('input_2')
        submit_button = self.browser.find_element_by_css_selector('.submit')
        edit_distance = self.browser.find_element_by_id('edit_distance').text
        self.assertEqual(edit_distance, '')

        # User types into inputs and submits form
        input_1.send_keys('kitten')
        input_2.send_keys('sitting')
        submit_button.click()

        # User sees placeholder contains minimum edit distance
        edit_distance = self.browser.find_element_by_id('edit_distance').text
        self.assertEqual(edit_distance, '3')

        # User types same phrase into inputs and submits form
        input_1.clear()
        input_2.clear()
        input_1.send_keys('harry')
        input_2.send_keys('harry')
        submit_button.click()

        # User sees placeholder contains minimum edit distance
        edit_distance = self.browser.find_element_by_id('edit_distance').text
        self.assertEqual(edit_distance, '0')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
