import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from TestSuites.testcases.testpages import IPGetStartedPage
from TestSuites.testcases.testpages import IPLoginPage
from TestSuites.testcases.testpages import IPSummaryPage
from TestSuites.testcases.testpages import IPInvestorTypePage
from TestSuites.testcases.testpages import IPEmploymentStatusPage
from TestSuites.testcases.testpages import IPInvestorAccredidationPage
from .testcaseutilities.testinfo import TestInfo


class TestIPInvestorAccredidation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4445/wd/hub',
             desired_capabilities=DesiredCapabilities.CHROME)
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_investor_accredidation_page = IPInvestorAccredidationPage(self.driver)
        ip_investor_accredidation_page.is_expected_landing_url()
        ip_investor_accredidation_page.divTypeNet_Worth.click()

        ip_investor_accredidation_page = IPInvestorAccredidationPage(self.driver)
        ip_investor_accredidation_page.is_expected_landing_url()
        ip_investor_accredidation_page.clickContinue()

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
