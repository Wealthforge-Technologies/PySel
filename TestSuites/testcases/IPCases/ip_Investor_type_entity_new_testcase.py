import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ..testpages.IPPages.ipinvestortypepage import IPInvestorTypePage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral


class TestIPInvestorEntity(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_investor_type_entity_new = IPInvestorTypePage(self.driver)
        ip_investor_type_entity_new.is_expected_landing_url()
        ip_investor_type_entity_new.divInvestorTypeEntity.click()

        ip_investor_type_entity_new.ddlEntityTypes.click()
        ip_investor_type_entity_new.clickContinue()


if __name__ == "__main__":
    unittest.main()
