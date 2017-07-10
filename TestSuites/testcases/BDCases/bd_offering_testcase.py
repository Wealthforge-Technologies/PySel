import unittest

from TestSuites.testcases.testpages.BDPages.bdhomepage import BDHomePage
from ..testcaseutilities.testinfo import TestInfo


class TestBDOffering(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_BD_offering(self):

        BDHomePage().clickOfferingTab()
        # bd_home_page.is_expected_landing_url()

        # bd_home_page.menuDashboardOffering.click()



if __name__ == "__main__":
    unittest.main()
