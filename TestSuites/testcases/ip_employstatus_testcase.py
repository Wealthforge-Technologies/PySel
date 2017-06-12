import unittest

from TestSuites.testcases.testpages.ipemploystatuspage import IPEmploymentStatusPage
from .testcaseutilities.testinfo import TestInfo


class TestIPEmploymentStatus(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_employstatus_page = IPEmploymentStatusPage()
        ip_employstatus_page.is_expected_landing_url()

        ip_employstatus_page.ddlInvestorEmploymentStatus.click()
        ip_employstatus_page.rbOtherOpportunitiesNo.click()
        ip_employstatus_page.btnContinue.click()



if __name__ == "__main__":
    unittest.main()
