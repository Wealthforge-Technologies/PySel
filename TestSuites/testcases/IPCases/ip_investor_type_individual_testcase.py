import unittest

from ..testpages.IPPages.ipinvestortypepage import IPInvestorTypePage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral

class TestIPInvestorIndividual(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):


        ip_investor_type_individual = IPInvestorTypePage()
        ip_investor_type_individual.is_expected_landing_url()
        ip_investor_type_individual.clickIndividual()

        IPGeneral().clickContinue()



if __name__ == "__main__":
    unittest.main()
