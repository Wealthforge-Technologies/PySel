import unittest

from TestSuites.testcases.testpages.ipinvestoraccredidationpage import IPInvestorAccredidationPage
from .testcaseutilities.testinfo import TestInfo


class TestIPInvestorAccredidation(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_investor_accredidation_page = IPInvestorAccredidationPage()
        ip_investor_accredidation_page.is_expected_landing_url()

        ip_investor_accredidation_page.divTypeNet_Worth.click()
        ip_investor_accredidation_page.btnContinue.click()


if __name__ == "__main__":
    unittest.main()
