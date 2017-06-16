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
from TestSuites.testcases.testpages import IPPaymentTypePage
from .testcaseutilities.testinfo import TestInfo


class TestPaymentTypePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4445/wd/hub',
             desired_capabilities=DesiredCapabilities.CHROME)
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_payment_type_page = IPPaymentTypePage(self.driver)
        ip_payment_type_page.is_expected_landing_url()
        ip_payment_type_page.divACH.click()

        ip_payment_type_page = IPPaymentTypePage(self.driver)
        ip_payment_type_page.is_expected_landing_url()
        ip_payment_type_page.regInfo(self.lookup.testinfo["ACHAcctName"],
                                     self.lookup.testinfo["ddlAccountTypes"],
                                     self.lookup.testinfo["ACHRoutNum"],
                                     self.lookup.testinfo["ACHRoutNumConf"],
                                     self.lookup.testinfo["ACHAcctNum"],
                                     self.lookup.testinfo["ACHAcctNumConf"])

        ip_payment_type_page.clickContinue()


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
