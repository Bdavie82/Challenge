import unittest
from selenium import webdriver


class Challenge1(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        # BDAVIE 3-19-2019
        # Since I run on a MAC I have to remove the .exe for things to run properly
        self.driver = webdriver.Chrome("../chromedriver")

    def teardown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge1(self):
        # code for test steps
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)


if __name__ == '__main__':
    unittest.main()
