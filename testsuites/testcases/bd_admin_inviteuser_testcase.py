import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .testpages.bdloginpage import BDLoginPage
from .testpages.bdhomepage import BDHomePage
from .testpages.bdadmintab_page import BDAdminTabPage
from .testpages.bdadmintab_user_page import BDAdminTabUserPage

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
        # bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]][1].click()
        #
        # #click on create user under WealthForgeSecurities BD
        # bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]][2][2].click()
        #
        # bd_admintab_user_page = BDAdminTabUserPage(self.driver)
        # bd_admintab_user_page.enter_info(self.lookup.testinfo["NewBDUser.First Name"], self.lookup.testinfo["NewBDUser.Last Name"], self.lookup.testinfo["NewBDUser.Email"])
        # bd_admintab_user_page.add_role(self.lookup.testinfo["NewBDUser.Role1"])
        # bd_admintab_user_page.submit()
        #
        #
        # bd_admintab_page.load_treenodes()
        # bd_admintab_page.treespace[self.lookup.testinfo["NewBDUser.Full Name"]].click()
        #
        # bd_admintab_user_page.first_name_should_be(self.lookup.testinfo["NewBDUser.First Name"])
        # bd_admintab_user_page.last_name_should_be(self.lookup.testinfo["NewBDUser.Last Name"])
        # bd_admintab_user_page.email_should_be(self.lookup.testinfo["NewBDUser.Email"])

        bd_admintab_page.treespace["F767 L82"].click()
        bd_admintab_user_page = BDAdminTabUserPage(self.driver)
        bd_admintab_user_page.first_name_should_be("F767")
        bd_admintab_user_page.last_name_should_be("L82")
        bd_admintab_user_page.email_should_be("wealthforgedev1+989928@gmail.com")
        bd_admintab_user_page.roles_should_contain("Fingerprinted Person")
        bd_admintab_user_page.roles_should_contain("Chief Compliance Officer")











    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
