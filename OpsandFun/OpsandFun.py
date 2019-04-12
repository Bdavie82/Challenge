import unittest

from Fi
from selenium import webdriver


class Loops(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        # BDAVIE 3-19-2019
        # Since I run on a MAC I have to remove the .exe for things to run properly
        self.driver = webdriver.Chrome("../chromedriver")

    def teardown(self):
        # code to close webdriver
        self.driver.close()

    def navigateToPage(self):
        self.driver.get("https://www.copart.com")

    def test_AssertCorrectPage(self):
        self.navigateToPage()
        # code for assert test
        self.assertIn("Copart USA", self.driver.title)

    def test_displayFib(self):
        Fib.fibcalc(5)


if __name__ == '__main__':
    unittest.main()
