import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ..testpages.IPPages.ipmarriedinvestorregistrationpage import IPMarriedInvestorRegistrationPage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral


class TestIPMarriedInvestorRegistration(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_investor_registration_married_page = IPMarriedInvestorRegistrationPage()
        ip_investor_registration_married_page.is_expected_landing_url()
        ip_investor_registration_married_page.enter_info(self.lookup.testinfo["txtInvestorFirstName"],
                                              self.lookup.testinfo["txtInvestorLastName"],
                                              self.lookup.testinfo["txtInvestorDOB"],
                                              self.lookup.testinfo["txtInvestorSSN"],
                                              self.lookup.testinfo["txtInvestorAddress1"],
                                              self.lookup.testinfo["txtInvestorAddress2"],
                                              self.lookup.testinfo["txtInvestorCity"],
                                              self.lookup.testinfo["ddlInvestorStateProvs"],
                                              self.lookup.testinfo["txtInvestorPostalCode"],
                                              self.lookup.testinfo["txtInvestorPhone"],
                                              self.lookup.testinfo["txtInvestorEmail"],
                                              self.lookup.testinfo["txtSpouseFirstName"],
                                              self.lookup.testinfo["txtSpouseLastName"],
                                              self.lookup.testinfo["txtSpouseDOB"],
                                              self.lookup.testinfo["txtSpouseSSN"],
                                              self.lookup.testinfo["txtSpousePhone"],
                                              self.lookup.testinfo["txtSpouseEmail"],
                                              self.lookup.testinfo["txtSpouseEmailConfirm"])

        IPGeneral().clickContinue()

if __name__ == "__main__":
    unittest.main()
