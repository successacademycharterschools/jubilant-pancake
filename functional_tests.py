from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_submit_form_returns_dist(self):
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
        edit_distance_box = self.browser.find_element_by_id('edit_distance').text
        self.assertEqual(edit_distance_box, '')

        # User types into first input
        input_1.send_keys('kitten')

        # User types into second input
        input_2.send_keys('sitting')

        # User submits form
        submit_button.click()

        # User sees placeholder contains minimum edit distance
        edit_distance_box = self.browser.find_element_by_id('edit_distance').text
        self.assertEqual(edit_distance_box, '3')

        # User types into first input
        # User types into second input
        # User submits form
        # User sees placeholder contains minimum edit distance
        self.fail('Finish test! Pancake not fully jubilant operational')

        # User quits browser
if __name__ == '__main__':
    unittest.main(warnings='ignore')
