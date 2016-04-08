from selenium import webdriver
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
        self.fail('Finish test! Pancake not fully jubilant operational')

        # User sees a paragraph about the site
        # User sees 2 text input fields and a centered placeholder
        # User types into first input
        # User types into second input
        # User submits form
        # User sees placeholder contains minimum edit distance

        # User types into first input
        # User types into second input
        # User submits form
        # User sees placeholder contains minimum edit distance

        # User quits browser
if __name__ == '__main__':
    unittest.main(warnings='ignore')
