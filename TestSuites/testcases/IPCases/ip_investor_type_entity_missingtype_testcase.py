import unittest

from ..testpages.IPPages.ipinvestortypepage import IPInvestorTypePage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral


class TestIPInvestorEntity(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_entitytypemissing(self):
        ip_investor_type_entity_missingtype = IPInvestorTypePage()
        ip_investor_type_entity_missingtype.is_expected_landing_url()
        ip_investor_type_entity_missingtype.clickEntity()

        ip_investor_type_entity_missingtype.clickNewEntity()

        IPGeneral().scrollToContinue()
        IPGeneral().clickContinue()


if __name__ == "__main__":
    unittest.main()
