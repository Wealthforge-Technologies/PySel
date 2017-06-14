import unittest

from ..testpages.IPPages.ipinvestorregistrationpage import IPInvestorTypePage
from ..testcaseutilities.testinfo import TestInfo


class TestIPInvestorRegistration(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_investor_registration_page = IPInvestorTypePage()
        ip_investor_registration_page.is_expected_landing_url()
        ip_investor_registration_page.enter_info(self.lookup.testinfo["txtInvestorFirstName"],
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


if __name__ == "__main__":
    unittest.main()
