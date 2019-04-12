import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


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

    def getPopular(self):
        wait = WebDriverWait(self.driver, 10)
        stuff = wait.until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, ".col-lg-3.col-sm-3.col-md-3.col-xs-6.col-xs-ext-sm")))
        popular = self.driver.find_element_by_css_selector("[ng-if=popularSearches]")
        makes_models = popular.find_elements_by_css_selector("a")

        for mm in makes_models:
            MM = mm.get_attribute('innerHTML')
            link = mm.get_attribute('href')
            print(MM + " - " + link)

        self.driver.implicitly_wait(15)

    def test_AssertCorrectPage(self):
        self.navigateToPage()
        # code for assert test
        self.assertIn("Copart USA", self.driver.title)

    def test_ListPopular(self):
        self.navigateToPage()
        self.getPopular()


if __name__ == '__main__':
    unittest.main()
