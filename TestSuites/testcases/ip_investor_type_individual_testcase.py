import unittest

from TestSuites.testcases.testpages.ipinvestortypepage import IPInvestorTypePage
from .testcaseutilities.testinfo import TestInfo


class TestIPInvestorIndividual(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_investor_type_individual = IPInvestorTypePage()
        ip_investor_type_individual.is_expected_landing_url()
        ip_investor_type_individual.btnInvTypeIndiv.click()

        ip_investor_type_individual.btnContinue.click()

    # def tearDown(self):
    #     self.driver.close()



if __name__ == "__main__":
    unittest.main()
