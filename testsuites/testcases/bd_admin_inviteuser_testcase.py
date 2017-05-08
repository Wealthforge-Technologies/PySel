import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .testpages.bdloginpage import BDLoginPage
from .testpages.bdhomepage import BDHomePage
from .testpages.bdadmintab_page import BDAdminTabPage
from .testcaseutilities.testinfo import TestInfo

class TestBDAdmin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4445/wd/hub',
             desired_capabilities=DesiredCapabilities.CHROME)
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_bd_admin(self):
        bd_login_page = BDLoginPage(self.driver)


        bd_login_page.land()
        bd_login_page.is_expected_landing_url()
        bd_login_page.login(self.lookup.testinfo["CCO.email"],self.lookup.testinfo["CCO.password"])

        bd_home_page = BDHomePage(self.driver)
        bd_home_page.is_expected_landing_url()
        bd_home_page.menuDashboardAdmin.click()

        bd_admintab_page = BDAdminTabPage(self.driver)
        bd_admintab_page.is_expected_landing_url()
        bd_admintab_page.load_treenodes()

        #click on dots
        bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]][1].click()

        #click on create user under WealthForgeSecurities BD
        bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]][2][2].click()

        while True:
            pass







    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
