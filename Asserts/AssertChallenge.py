import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Asserts(unittest.TestCase):

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

    def searchTerm(self):
        search_input = self.driver.find_element_by_id("input-search")
        search_input.send_keys('exotics')

    def search(self):

        search_button = self.driver.find_element_by_class_name("btn-lightblue")
        search_button.click()

    def findData(self, data):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[data-uname=lotsearchLotmake]")))

        elms = self.driver.find_elements_by_css_selector("[data-uname=lotsearchLotmake]")

        for e in elms:
            data_element = e.get_attribute('innerHTML')
            if data_element == data:
                print(data + " found")
                return True
                break
            elif data_element != data:
                print(data + " not found")

    def test_AssertCorrectPage(self):
        self.navigateToPage()
        # code for assert test
        self.assertIn("Copart USA", self.driver.title)

    def test_FindPorsche(self):
        self.navigateToPage()
        self.searchTerm()
        self.search()
        self.assertIs(self.findData('PORSCHE'), True)


if __name__ == '__main__':
    unittest.main()
