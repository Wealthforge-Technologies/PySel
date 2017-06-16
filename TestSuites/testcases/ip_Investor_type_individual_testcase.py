import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from TestSuites.testcases.testpages import IPInvestorTypePage
from .testcaseutilities.testinfo import TestInfo


class TestIPInvestorIndividual(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_investor_type_individual_page = IPInvestorTypePage(self.driver)
        ip_investor_type_individual_page.is_expected_landing_url()

        ip_investor_type_individual_page.divInvestorTypeIndividual.click()
        ip_investor_type_individual_page.clickContinue()

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
