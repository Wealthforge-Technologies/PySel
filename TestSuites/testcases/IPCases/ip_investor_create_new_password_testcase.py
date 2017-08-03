import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ..testpages.IPPages.ipentityinvestorregistrationpage import IPCreateNewPasswordPage
from ..testcaseutilities.testinfo import TestInfo

class IPCreateNewPassword(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_investor_create_new_password_page = IPCreateNewPasswordPage()
        ip_investor_create_new_password_page.is_expected_landing_url()
        ip_investor_create_new_password_page.enter_info(self.lookup.testinfo["username"],
                                                     self.lookup.testinfo["password2"])

        ip_investor_create_new_password_page().btnCreateAcct()

        ip_investor_create_new_password_page().btnReturnToLogin()

if __name__ == "__main__":
    unittest.main()
