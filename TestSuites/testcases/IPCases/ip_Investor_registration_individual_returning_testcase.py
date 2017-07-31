import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from TestSuites.testcases.testpages import IPInvestorRegistrationPage
from .testcaseutilities.testinfo import TestInfo


class TestIPIndividualInvestorRegistrationReturning(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_investor_registration_individual_returning_page = IPInvestorRegistrationPage()
        ip_investor_registration_individual_returning_page.is_expected_landing_url()
        ip_investor_registration_individual_returning_page.verify_info(self.lookup.testinfo["txtInvestorFirstName"],
                                                         self.lookup.testinfo["txtInvestorLastName"],
                                                         self.lookup.testinfo["txtInvestorDOB"],
                                                         self.lookup.testinfo["txtInvestorSSN"],
                                                         self.lookup.testinfo["txtInvestorAddress1"],
                                                         self.lookup.testinfo["txttxtInvestorAddress2"],
                                                         self.lookup.testinfo["txtInvestorCity"],
                                                         self.lookup.testinfo["ddlInvestorStateProvs"],
                                                         self.lookup.testinfo["txtInvestorPostalCode"],
                                                         self.lookup.testinfo["txtInvestorPhone"],
                                                         self.lookup.testinfo["txtInvestorEmail"])

        ip_investor_registration_individual_returning_page.clickContinue()

if __name__ == "__main__":
    unittest.main()
