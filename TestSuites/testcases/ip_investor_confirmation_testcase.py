import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from TestSuites.testcases.testpages import IPInvestorConfirmationPage
from .testcaseutilities.testinfo import TestInfo


class IPInvestorConfirmationPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4445/wd/hub',
             desired_capabilities=DesiredCapabilities.CHROME)
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_payment_type_page = IPInvestorConfirmationPage(self.driver)
        ip_payment_type_page.is_expected_landing_url()
        ip_payment_type_page.chkBoxAffirmCC.click()

        ip_payment_type_page.chkBoxAffirmTC.click()

        ip_payment_type_page.clickContinue()


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
