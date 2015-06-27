import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class UrlTests(unittest.TestCase):
    def setUp(self):
        BASE_URL = 'http://weathertrack.mybluemix.net'
        self.browser = webdriver.Firefox()        
    
    def test_hello_flask_URL_navigates_to_correct_page(self):
        self.browser.get(BASE_URL + '/hello')
        text = self.browser.find_element(By.XPATH, '/html/body/text()')
        self.assertEqual("Hello!", text, "Title of /hello page didn't match test")
        
    def test_hello_name_URL_returns_correct_resource(self):
        self.browser.get(BASE_URL + "/hello/Hayden")
        text = self.browser.find_element(By.XPATH, '/html/body/text()')
        self.assertEqual("Hello Hayden", text)
        
    def test_temperature_api_URL_page_loads_correctly(self):
        self.browser.get(BASE_URL + '/api/temperature/lenexa/ks'
        self.assertEqual("WeatherTrack", self.browser.title)
        
    def test_base_URL_returns_temperature_retrieval_page(self):
        self.browser.get(BASE_URL)
        self.assertEqual("WeatherTrack", self.browser.title)
        
    def tearDown(self):
        self.browser.close()
