import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/elena/Documents/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = 'https://clinician.sense.ly'

    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()
