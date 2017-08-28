import unittest

from ..testpages.OEPages.oeinvestorentitypage import OEInvestorEntityPage
from ..testcaseutilities.testinfo import TestInfo


class TestInvestorEntity(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):
        oe_investor_entity_page = OEInvestorEntityPage()

        oe_investor_entity_page.land()
        oe_investor_entity_page.is_expected_landing_url()

        oe_investor_entity_page.enter_info(self.lookup.testinfo["accreditType"],
                               self.lookup.testinfo["name"],
                               self.lookup.testinfo["signatoryName"],
                               self.lookup.testinfo["signatoryTitle"],
                               self.lookup.testinfo["ein"],
                               self.lookup.testinfo["cik"],
                               self.lookup.testinfo["street1"],
                               self.lookup.testinfo["city"],
                               self.lookup.testinfo["stateProvence"],
                               self.lookup.testinfo["zipCode"],
                               self.lookup.testinfo["primaryPhone"],
                               self.lookup.testinfo["email"]
                               )

        oe_investor_entity_page.clickForward()


if __name__ == "__main__":
    unittest.main()
