import unittest

from ..testpages.IPPages.ipinvestoraccredidationpage import IPInvestorAccredidationPage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral

class TestIPInvestorEntityAccredidation(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        accr = IPInvestorAccredidationPage()
        accr.is_expected_landing_url()

        accr.btnIncOrNet.click()

        IPGeneral().clickContinue()

if __name__ == "__main__":
    unittest.main()
