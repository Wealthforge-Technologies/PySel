import unittest

from TestSuites.testcases.testpages.ipinvestorsuitabilitypage import IPInvestorSuitabilityPage
from .testcaseutilities.testinfo import TestInfo


class TestIPInvestorSuitability(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_investor_suitability_page = IPInvestorSuitabilityPage()
        ip_investor_suitability_page.is_expected_landing_url()
        ip_investor_suitability_page.regInfo(self.lookup.testinfo["sq-10"],
                                             self.lookup.testinfo["sq-20"],
                                             self.lookup.testinfo["sq-30"],
                                             self.lookup.testinfo["sq-40"],
                                             self.lookup.testinfo["sq-50"],
                                             self.lookup.testinfo["sq-60"],
                                             self.lookup.testinfo["sq-70"],
                                             self.lookup.testinfo["sq-80"],
                                             self.lookup.testinfo["sq-90"],
                                             self.lookup.testinfo["sq-100"],
                                             self.lookup.testinfo["sq-110"],
                                             self.lookup.testinfo["sq-120"],
                                             self.lookup.testinfo["sq-130"])

        ip_investor_suitability_page.regInfo(self.lookup.testinfo["invAmnt"])

        ip_investor_suitability_page.investAmount.click()

        ip_investor_suitability_page.btnContinue.click()


if __name__ == "__main__":
    unittest.main()
