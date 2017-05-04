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
sys.path.append(os.path.abspath('../Utilities'))
from __init__ import driver
from Utit import *
from Users import *


class TestBDAdmin(unittest.TestCase):

    def setUp(self):
        self.users = Users()
        self.users.load_defaults()

    def test_BD_admin(self):
        bd_page = page.BDPage(driver())
        bd_rad_page = page.BDRadPage(driver())

        try:
            wait = WebDriverWait(driver(), 5).until(
                EC.title_contains(bd_page.expected_title))
        finally:
            bd_page.is_expected_title()

        #This should send us to BDRadPage
        bd_page.menuDashboardAdmin.click()
        Utit.waitForAngular(driver())

        try:
            wait = WebDriverWait(driver(), 5).until(
                lambda wait: driver().current_url == bd_rad_page.expected_landing_url)
        finally:
            bd_rad_page.is_expected_landing_url()

    def tearDown(self):
        # driver().close()
        pass


if __name__ == "__main__":
    unittest.main()
