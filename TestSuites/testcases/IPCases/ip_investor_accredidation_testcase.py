import unittest

from ..testpages.IPPages.ipinvestoraccredidationpage import IPInvestorAccredidationPage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral

class TestIPInvestorAccredidation(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):
        accr = IPInvestorAccredidationPage()
        accr.is_expected_landing_url()

        accr.btnNetWorth.click()

        IPGeneral().clickContinue()

if __name__ == "__main__":
    unittest.main()
