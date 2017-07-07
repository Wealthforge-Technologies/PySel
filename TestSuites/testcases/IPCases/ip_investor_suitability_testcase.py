import unittest

from ..testpages.IPPages.ipinvestorsuitabilitypage import IPInvestorSuitabilityPage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral


class TestIPInvestorSuitability(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        suitability = IPInvestorSuitabilityPage()
        suitability.is_expected_landing_url()
        suitability.enter_info(self.lookup.testinfo["sq-10"],
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
                                             self.lookup.testinfo["sq-130"]
                               )

        suitability.invest(self.lookup.testinfo["invAmnt"])

        IPGeneral().clickContinue()



if __name__ == "__main__":
    unittest.main()