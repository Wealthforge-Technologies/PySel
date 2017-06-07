import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .testpages.bdloginpage import BDLoginPage
from .testpages.bdhomepage import BDHomePage
from .testcaseutilities.testinfo import TestInfo


class TestBDBank(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_BD_bank(self):

        bd_home_page = BDHomePage()
        bd_home_page.is_expected_landing_url()
        bd_home_page.menuDashboardBankSetup.click()



if __name__ == "__main__":
    unittest.main()
