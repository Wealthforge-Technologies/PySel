import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from TestSuites.testcases.testpages import IPInvestorTypePage
from .testcaseutilities.testinfo import TestInfo


class TestIPInvestorMarried(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_investor_type_married = IPInvestorTypePage(self.driver)
        ip_investor_type_married.is_expected_landing_url()
        ip_investor_type_married.divInvestorTypeMarried.click()

        ip_investor_type_married.entityType.click()
        ip_investor_type_married.clickContinue()

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
