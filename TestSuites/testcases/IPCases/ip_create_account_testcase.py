import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ..testpages.IPPages.ipcreateanaccountpage import IPCreateAnAccountPage
from ..testcaseutilities.testinfo import TestInfo

class IPCreateAnAccount(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):

        ip_investor_create_account_page = IPCreateAnAccountPage()
        ip_investor_create_account_page.is_expected_landing_url()
        ip_investor_create_account_page.enter_info(self.lookup.testinfo["fname"],
                                                     self.lookup.testinfo["lname"],
                                                     self.lookup.testinfo["email"],
                                                     self.lookup.testinfo["confemail"])

        ip_investor_create_account_page.btnCreateAcct.click()



        # ip_investor_create_account_page.btnReturnToLogin()

if __name__ == "__main__":
    unittest.main()
