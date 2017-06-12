import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from TestSuites.testcases.testpages import IPGetStartedPage
from TestSuites.testcases.testpages import IPLoginPage
from TestSuites.testcases.testpages import IPSummaryPage
from TestSuites.testcases.testpages import IPInvestorTypePage
from .testcaseutilities.testinfo import TestInfo


class TestIPInvestorIndividual(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Remote(
        #      command_executor='http://127.0.0.1:4445/wd/hub',
        #      desired_capabilities=DesiredCapabilities.CHROME)
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_login_page = IPLoginPage()

        ip_login_page.land()
        ip_login_page.is_expected_landing_url()
        ip_login_page.login(self.lookup.testinfo["IP.email"],self.lookup.testinfo["IP.password"])

        ip_home_page = IPGetStartedPage()
        ip_home_page.is_expected_landing_url()
        ip_home_page.btnStart.click()

        ip_summary_page = IPSummaryPage()
        ip_summary_page.is_expected_landing_url()
        ip_summary_page.btnContinue.click()

        ip_investor_type_individual = IPInvestorTypePage()
        ip_investor_type_individual.is_expected_landing_url()
        ip_investor_type_individual.btnInvTypeIndiv.click()

        ip_investor_type_continue_page = IPInvestorTypePage()
        ip_investor_type_continue_page.is_expected_landing_url()
        ip_investor_type_continue_page.btnContinue.click()

    # def tearDown(self):
    #     self.driver.close()



if __name__ == "__main__":
    unittest.main()
