import unittest
from selenium import webdriver


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def test_hello_flask_URL_navigates_to_correct_page(self):
        self.browser.get('http://weathertrack.mybluemix.net')
        self.assertEqual("Hello!", self.browser.title, "Title of /hello page didn't match test")
        
    def tearDown(self):
        self.browser.quit()