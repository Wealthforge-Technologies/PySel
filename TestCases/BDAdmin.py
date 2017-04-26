import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import os
import time
# This lets us import modules from sibling directories
sys.path.append(os.path.abspath('../Pages'))
import page


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4445/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def test_BD_admin(self):
        login_page = page.LoginPage(self.driver)
        bd_page = page.BDPage(self.driver)

        #start login_page
        self.driver.get(login_page.url)
        login_page.is_title_matches()
        login_page.email = "oquelland@wealthforge.com"
        login_page.password = "Test123!"
        #login_page.submit()
        login_page.btnLogin.click()

        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains("WF: Broker Dealer"))
        finally:
            assert "WF: Broker Dealer" in self.driver.title

        #Start bd_page
        try:
            wait = WebDriverWait(self.driver, 5).until(
                lambda driver: bd_page.menuDashboardAdmin is not None)
        finally:
            #self.driver.find_element_by_id('menuDashboardAdmin').click()
            bd_page.menuDashboardAdmin.click()

        #bd_page.menuDashboardAdmin.click()

        try:
            wait = WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.current_url == 'https://qa1.wealthforge.org/BD/#/rad')
        finally:
            assert "https://qa1.wealthforge.org/BD/#/rad" in self.driver.current_url

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
