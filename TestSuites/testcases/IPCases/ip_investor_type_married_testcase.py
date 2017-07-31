import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ..testpages.IPPages.ipinvestortypepage import IPInvestorTypePage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral


class TestIPInvestorMarried(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_married(self):
        ip_investor_type_married = IPInvestorTypePage()
        ip_investor_type_married.is_expected_landing_url()
        ip_investor_type_married.clickMarried()

        IPGeneral().clickContinue()



if __name__ == "__main__":
    unittest.main()
