import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from ..testpages.BDPages.bdloginpage import BDLoginPage
from ..testpages.BDPages.bdhomepage import BDHomePage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.NWPages.nwhomepage import NWHomePage

class TestNWLogin(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_nw_login(self):

        # New for network
        nw_home_page = NWHomePage()
        nw_home_page.land()
        nw_home_page.is_expected_landing_url()
        nw_home_page.is_expected_title()
        # nw_home_page.menuDashboardAdmin.click() # TODO

    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()
