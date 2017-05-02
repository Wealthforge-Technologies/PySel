import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import os
import time
sys.path.append(os.path.abspath('../Pages'))
sys.path.append(os.path.abspath('../Utilities'))
import page
from Utit import *
from Users import *


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4445/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.users = Users()
        self.users.load_defaults()

    def test_login(self):
        login_page = page.LoginPage(self.driver)
        bd_page = page.BDPage(self.driver)

        self.driver.get(login_page.url)
        Utit.waitForAngular(self.driver)

        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(login_page.expected_title))
        finally:
            login_page.is_expected_title()

        login_page.email.send_keys(self.users.lookup["CCO.email"])
        assert self.users.lookup["CCO.email"] in login_page.email.get_attribute("value")

        login_page.password.send_keys(self.users.lookup["CCO.password"])
        assert self.users.lookup["CCO.password"] in login_page.password.get_attribute("value")

        login_page.submit()
        Utit.waitForAngular(self.driver)

        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(bd_page.expected_title))
        finally:
            bd_page.is_expected_title()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
