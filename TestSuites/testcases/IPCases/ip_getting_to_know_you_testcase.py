import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from TestSuites.testcases.testpages import IPGettingToKnowYouPage
from .testcaseutilities.testinfo import TestInfo


class TestIPGettingToKnowYou(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_investor_registration_individual_page = IPGettingToKnowYouPage(self.driver)
        ip_investor_registration_individual_page.is_expected_landing_url()
        ip_investor_registration_individual_page.regInfo(self.lookup.testinfo["address"],
                                                         self.lookup.testinfo["addressCont"],
                                                         self.lookup.testinfo["city"],
                                                         self.lookup.testinfo["stateDrop"],
                                                         self.lookup.testinfo["zip"],
                                                         self.lookup.testinfo["phone"])

        ip_investor_registration_individual_page.clickContinue()

if __name__ == "__main__":
    unittest.main()
