import unittest

from TestSuites.testcases.testpages.ipsummarypage import IPSummaryPage
from .testcaseutilities.testinfo import TestInfo


class TestIPSummary(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_summary_page = IPSummaryPage()
        ip_summary_page.is_expected_landing_url()
        ip_summary_page.btnContinue.click()


if __name__ == "__main__":
    unittest.main()
