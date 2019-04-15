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

    def navigate_to_page(self):
        self.driver.get("https://www.copart.com")

    def test_assert_correct_page(self):
        self.navigate_to_page()
        # code for assert test
        self.assertIn("Copart USA", self.driver.title)

    def test_display_fib(self):
        des_seq = 4
        num = Fib().fibcalc(des_seq - 1)
        word = N2W(num)

        print(str(num) + ' - ' + word)


if __name__ == '__main__':
    unittest.main()
