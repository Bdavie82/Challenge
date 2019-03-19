import unittest
from selenium import webdriver


class Asserts(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        # BDAVIE 3-19-2019
        # Since I run on a MAC I have to remove the .exe for things to run properly
        self.driver = webdriver.Chrome("../chromedriver")

    def teardown(self):
        # code to close webdriver
        self.driver.close()

    def Assert(self):
        # code for assert test
        self.driver.get("copart.com")
        self.assertIn("Copart USA", self.driver.title)


if __name__ == '__main__':
    unittest.main()
