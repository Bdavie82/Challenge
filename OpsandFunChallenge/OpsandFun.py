import unittest

from num2words import num2words as N2W
from selenium import webdriver

from OpsandFunChallenge.Fib import Fib


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
        num = Fib().fibcalc(9)
        word = N2W(num)

        print(str(num) + ' - ' + word)


if __name__ == '__main__':
    unittest.main()
