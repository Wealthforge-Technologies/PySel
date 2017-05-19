import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .testpages.bdloginpage import BDLoginPage
from .testpages.bdhomepage import BDHomePage
from .testcaseutilities.testinfo import TestInfo
from .testpages.nwhomepage import NWHomePage

class TestNWLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4445/wd/hub',
             desired_capabilities=DesiredCapabilities.CHROME)
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_nw_login(self):
        bd_login_page = BDLoginPage(self.driver)

        bd_login_page.land()
        bd_login_page.is_expected_landing_url()
        bd_login_page.login(self.lookup.testinfo["CCO.email"],self.lookup.testinfo["CCO.password"])

        # New for network
        nw_home_page = NWHomePage(self.driver)
        nw_home_page.land()
        nw_home_page.is_expected_landing_url()
        nw_home_page.is_expected_title()
        # nw_home_page.menuDashboardAdmin.click() # TODO

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
