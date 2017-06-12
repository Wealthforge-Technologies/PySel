import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from TestSuites.testcases.testpages import IPGetStartedPage
from TestSuites.testcases.testpages import IPLoginPage
from TestSuites.testcases.testpages import IPSummaryPage
from TestSuites.testcases.testpages import IPInvestorTypePage
from TestSuites.testcases.testpages import IPEmploymentStatusPage
from .testcaseutilities.testinfo import TestInfo


class TestIPEmploymentStatus(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4445/wd/hub',
             desired_capabilities=DesiredCapabilities.CHROME)
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_login_page = IPLoginPage(self.driver)

        ip_login_page.land()
        ip_login_page.is_expected_landing_url()
        ip_login_page.login(self.lookup.testinfo["IP.email"],self.lookup.testinfo["IP.password"])

        ip_home_page = IPGetStartedPage(self.driver)
        ip_home_page.is_expected_landing_url()
        ip_home_page.btnStart.click()

        ip_summary_page = IPSummaryPage(self.driver)
        ip_summary_page.is_expected_landing_url()
        ip_summary_page.btnContinue.click()

        ip_investor_type_individual = IPInvestorTypePage(self.driver)
        ip_investor_type_individual.is_expected_landing_url()
        ip_investor_type_individual.btnInvTypeIndiv.click()

        ip_investor_type_continue_page = IPInvestorTypePage(self.driver)
        ip_investor_type_continue_page.is_expected_landing_url()
        ip_investor_type_continue_page.btnContinue.click()

        ip_investor_registration_page = IPInvestorRegistrationPage(self.driver)
        ip_investor_registration_page.is_expected_landing_url()
        ip_investor_registration_page.regInfo(self.lookup.testinfo["txtInvestorFirstName"],self.lookup.testinfo["txtInvestorLastName"],self.lookup.testinfo["txtInvestorDOB"],self.lookup.testinfo["txtInvestorSSN"],self.lookup.testinfo["txtInvestorAddress1"],self.lookup.testinfo["txttxtInvestorAddress2"],self.lookup.testinfo["txtInvestorCity"],self.lookup.testinfo["ddlInvestorStateProvs"],self.lookup.testinfo["txtInvestorPostalCode"],self.lookup.testinfo["txtInvestorPhone"],self.lookup.testinfo["txtInvestorEmail"])

        ip_employstatus_page = IPEmploymentStatusPage(self.driver)
        ip_employstatus_page.is_expected_landing_url()
        ip_employstatus_page.ddlInvestorEmploymentStatus.click()

        ip_employstatus_page = IPEmploymentStatusPage(self.driver)
        ip_employstatus_page.is_expected_landing_url()
        ip_employstatus_page.rbOtherOpportunitiesNo.click()

        ip_employstatus_page = IPEmploymentStatusPage(self.driver)
        ip_employstatus_page.is_expected_landing_url()
        ip_employstatus_page.btnContinue.click()

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
