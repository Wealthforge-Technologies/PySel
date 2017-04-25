import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import os
import time
sys.path.append(os.path.abspath('../Pages'))
import page


class IPLogin(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4445/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)
    self.driver.get("https://qa1.wealthforge.org/login/#/")

  def test_login(self):
    login_page = page.QALoginPage(self.driver)
    login_page.is_title_matches()
    login_page.email = "oquelland@wealthforge.com"
    print(login_page.email)
    login_page.password = "Test123!"
    print(login_page.password)
    # login_page.btnsubmit.click()
    login_page.submit()
    time.sleep(10)

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
