import unittest

from ..testpages.IPPages.ipsummarypage import IPSummaryPage
from ..testcaseutilities.testinfo import TestInfo

class TestIPInvestMinNotMet(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_summary_page = IPSummaryPage()
        ip_summary_page.is_expected_landing_url()

        ip_summary_page.enter_info(self.lookup.testinfo["invAmnt"])

        ip_summary_page().btnInvestAmount()

if __name__ == "__main__":
    unittest.main()
