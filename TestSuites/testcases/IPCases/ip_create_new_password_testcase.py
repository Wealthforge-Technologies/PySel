import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ..testpages.IPPages.ipcreatenewpassword import IPCreateNewPasswordPage
from ..testcaseutilities.testinfo import TestInfo
from ..testcaseutilities.gmailaccessor import get_new_ip_user_password_reset_url

class IPCreateNewPassword(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):
        # print(self.lookup.testinfo["email"])

        ip_investor_create_new_password_page = IPCreateNewPasswordPage(get_new_ip_user_password_reset_url(self.lookup.testinfo["email"]))
        ip_investor_create_new_password_page.land()
        ip_investor_create_new_password_page.is_expected_landing_url()
        ip_investor_create_new_password_page.enter_info(self.lookup.testinfo["username"],
                                                        self.lookup.testinfo["password2"])

        ip_investor_create_new_password_page.clickSave()

        ip_investor_create_new_password_page.clickReturnLogin()

if __name__ == "__main__":
    unittest.main()
