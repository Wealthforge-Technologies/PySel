import unittest

from ..testpages.IPPages.ipsummarypage import IPSummaryPage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral

class TestIPSummary(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):

        ip_summary_page = IPSummaryPage()
        ip_summary_page.is_expected_landing_url()

        IPGeneral().clickContinue()


if __name__ == "__main__":
    unittest.main()
