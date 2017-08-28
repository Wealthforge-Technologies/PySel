import unittest

from ..testpages.OEPages.oeinvestorindividualpage import OEInvestorIndividualPage
from ..testcaseutilities.testinfo import TestInfo


class TestInvestorIndividual(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):
        oe_investor_individual_page = OEInvestorIndividualPage()

        oe_investor_individual_page.land()
        oe_investor_individual_page.is_expected_landing_url()

        oe_investor_individual_page.enter_info(self.lookup.testinfo["accreditType"],
                               self.lookup.testinfo["firstName"],
                               self.lookup.testinfo["lastName"],
                               self.lookup.testinfo["dateOfBirth"],
                               self.lookup.testinfo["socialSN"],
                               self.lookup.testinfo["phoneNumber"],
                               self.lookup.testinfo["email"],
                               self.lookup.testinfo["streetAddress"],
                               self.lookup.testinfo["city"],
                               self.lookup.testinfo["stateProvence"],
                               self.lookup.testinfo["zipCode"]
                               )

        oe_investor_individual_page.clickForward()


if __name__ == "__main__":
    unittest.main()
