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
from TestSuites.testcases.testpages import IPDocumentUploadPage
from .testcaseutilities.testinfo import TestInfo


class TestDocumentUploadPage(unittest.TestCase):
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

        ip_investor_registration_page = IPInvestorRegistrationPage()
        ip_investor_registration_page.is_expected_landing_url()
        ip_investor_registration_page.regInfo(self.lookup.testinfo["txtInvestorFirstName"],self.lookup.testinfo["txtInvestorLastName"],self.lookup.testinfo["txtInvestorDOB"],self.lookup.testinfo["txtInvestorSSN"],self.lookup.testinfo["txtInvestorAddress1"],self.lookup.testinfo["txttxtInvestorAddress2"],self.lookup.testinfo["txtInvestorCity"],self.lookup.testinfo["ddlInvestorStateProvs"],self.lookup.testinfo["txtInvestorPostalCode"],self.lookup.testinfo["txtInvestorPhone"],self.lookup.testinfo["txtInvestorEmail"])

        ip_employstatus_page = IPEmploymentStatusPage()
        ip_employstatus_page.is_expected_landing_url()
        ip_employstatus_page.ddlInvestorEmploymentStatus.click()

        ip_employstatus_page = IPEmploymentStatusPage()
        ip_employstatus_page.is_expected_landing_url()
        ip_employstatus_page.rbOtherOpportunitiesNo.click()

        ip_employstatus_page = IPEmploymentStatusPage()
        ip_employstatus_page.is_expected_landing_url()
        ip_employstatus_page.btnContinue.click()

        ip_investor_accredidation_page = IPInvestorAccredidationPage()
        ip_investor_accredidation_page.is_expected_landing_url()
        ip_investor_accredidation_page.divTypeNet_Worth.click()

        ip_investor_accredidation_page = IPInvestorAccredidationPage()
        ip_investor_accredidation_page.is_expected_landing_url()
        ip_investor_accredidation_page.btnContinue.click()

        ip_investor_suitability_page = IPInvestorSuitabilityPage()
        ip_investor_suitability_page.is_expected_landing_url()
        ip_investor_suitability_page.regInfo(self.lookup.testinfo["sq-10"], self.lookup.testinfo["sq-20"], self.lookup.testinfo["sq-30"], self.lookup.testinfo["sq-40"], self.lookup.testinfo["sq-50"], self.lookup.testinfo["sq-60"], self.lookup.testinfo["sq-70"], self.lookup.testinfo["sq-80"], self.lookup.testinfo["sq-90"], self.lookup.testinfo["sq-100"], self.lookup.testinfo["sq-110"], self.lookup.testinfo["sq-120"], self.lookup.testinfo["sq-130"])

        ip_investor_suitability_page = IPInvestorSuitabilityPage()
        ip_investor_suitability_page.is_expected_landing_url()
        ip_investor_suitability_page.regInfo(self.lookup.testinfo["invAmnt"])

        ip_investor_suitability_page = IPInvestorSuitabilityPage()
        ip_investor_suitability_page.is_expected_landing_url()
        ip_investor_suitability_page.investAmount.click()

        ip_investor_suitability_page = IPInvestorSuitabilityPage()
        ip_investor_suitability_page.is_expected_landing_url()
        ip_investor_suitability_page.btnContinue.click()

        ip_document_upload_page = IPDocumentUploadPage()
        ip_document_upload_page.is_expected_landing_url()
        ip_document_upload_page.fileBox.click()

        ip_document_upload_page = IPDocumentUploadPage()
        ip_document_upload_page.is_expected_landing_url()
        ip_document_upload_page.btnContinue.click()


    # def tearDown(self):
    #     self.driver.close()



if __name__ == "__main__":
    unittest.main()
