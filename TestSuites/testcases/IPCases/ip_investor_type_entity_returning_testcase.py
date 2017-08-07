import unittest

from ..testpages.IPPages.ipinvestortypepage import IPInvestorTypePage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral


class TestIPInvestorEntityReturning(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_entitytype(self):
        ip_investor_type_entity_returning = IPInvestorTypePage()
        ip_investor_type_entity_returning.is_expected_landing_url()
        ip_investor_type_entity_returning.clickEntity()

        ip_investor_type_entity_returning.clickReturnEntityByName(self.lookup.testinfo["txtInvestorName"])

        IPGeneral().scrollToContinue()
        IPGeneral().clickContinue()


if __name__ == "__main__":
    unittest.main()
