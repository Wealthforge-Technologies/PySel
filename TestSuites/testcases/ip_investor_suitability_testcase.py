import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from TestSuites.testcases.testpages import IPGetStartedPage
from TestSuites.testcases.testpages import IPLoginPage
from TestSuites.testcases.testpages import IPSummaryPage
from TestSuites.testcases.testpages import IPInvestorTypePage
from TestSuites.testcases.testpages import IPEmploymentStatusPage
from TestSuites.testcases.testpages import IPInvestorAccredidationPage
from TestSuites.testcases.testpages import IPInvestorSuitabilityPage
from .testcaseutilities.testinfo import TestInfo


class TestIPInvestorSuitability(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4445/wd/hub',
             desired_capabilities=DesiredCapabilities.CHROME)
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):


        ip_investor_suitability_page = IPInvestorSuitabilityPage(self.driver)
        ip_investor_suitability_page.is_expected_landing_url()
        ip_investor_suitability_page.regInfo(self.lookup.testinfo["sq-10"], self.lookup.testinfo["sq-20"], self.lookup.testinfo["sq-30"], self.lookup.testinfo["sq-40"], self.lookup.testinfo["sq-50"], self.lookup.testinfo["sq-60"], self.lookup.testinfo["sq-70"], self.lookup.testinfo["sq-80"], self.lookup.testinfo["sq-90"], self.lookup.testinfo["sq-100"], self.lookup.testinfo["sq-110"], self.lookup.testinfo["sq-120"], self.lookup.testinfo["sq-130"])

        ip_investor_suitability_page = IPInvestorSuitabilityPage(self.driver)
        ip_investor_suitability_page.is_expected_landing_url()
        ip_investor_suitability_page.regInfo(self.lookup.testinfo["invAmnt"])

        ip_investor_suitability_page = IPInvestorSuitabilityPage(self.driver)
        ip_investor_suitability_page.is_expected_landing_url()
        ip_investor_suitability_page.investAmount.click()

        ip_investor_suitability_page = IPInvestorSuitabilityPage(self.driver)
        ip_investor_suitability_page.is_expected_landing_url()
        ip_investor_suitability_page.clickContinue()

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
