import unittest

from ..testpages.IPPages.ipinvestortypepage import IPInvestorTypePage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral


class TestIPInvestorEntity(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_entitytype(self):
        ip_investor_type_entity_new = IPInvestorTypePage()
        ip_investor_type_entity_new.is_expected_landing_url()
        ip_investor_type_entity_new.btnInvTypeEntity.click()

        ip_investor_type_entity_new.enter_info(self.lookup.testinfo["ddlEntityTypes"])

        IPGeneral().scrollToContinue()
        IPGeneral().clickContinue()


if __name__ == "__main__":
    unittest.main()
