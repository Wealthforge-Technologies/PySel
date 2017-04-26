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


class Login(unittest.TestCase):

    def wait_for_angular(self, selenium):
        self.selenium.set_script_timeout(10)
        self.selenium.execute_async_script("""
      callback = arguments[arguments.length - 1];
      angular.element('wfApp').injector().get('$browser').notifyWhenNoOutstandingRequests(callback);""")

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4445/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def test_login(self):
        login_page = page.LoginPage(self.driver)
        self.driver.get(login_page.url)
        login_page.is_title_matches()
        login_page.email = "oquelland@wealthforge.com"
        login_page.password = "Test123!"
        login_page.submit()
        Utit.waitForAngular(self.driver)
        # try:
        #   wait = WebDriverWait(self.driver, 5).until(
        #       EC.title_contains("WF: Broker Dealer"))
        # finally:
        assert "WF: Broker Dealer" in self.driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
