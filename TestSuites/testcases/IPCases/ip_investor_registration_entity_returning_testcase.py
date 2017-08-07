import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ..testpages.IPPages.ipentityinvestorregistrationpage import IPEntityInvestorRegistrationPage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral

class IPReturningEntityInvestorRegistration(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):

        ip_investor_registration_entity_returning_page = IPEntityInvestorRegistrationPage()
        ip_investor_registration_entity_returning_page.is_expected_landing_url()
        ip_investor_registration_entity_returning_page.verify_info(self.lookup.testinfo["txtInvestorName"],
                                                     self.lookup.testinfo["txtInvestorSignatoryName"],
                                                     self.lookup.testinfo["txtInvestorSignatoryTitle"],
                                                     self.lookup.testinfo["txtInvestorEIN"],
                                                     self.lookup.testinfo["txtInvestorSSN"],
                                                     self.lookup.testinfo["txtInvestorAddress1"],
                                                     self.lookup.testinfo["txtInvestorAddress2"],
                                                     self.lookup.testinfo["txtInvestorCity"],
                                                     self.lookup.testinfo["ddlInvestorStateProvs"],
                                                     self.lookup.testinfo["txtInvestorPostalCode"],
                                                     self.lookup.testinfo["txtInvestorPhone"],
                                                     self.lookup.testinfo["txtInvestorEmail"])

        IPGeneral().clickContinue()

if __name__ == "__main__":
    unittest.main()
