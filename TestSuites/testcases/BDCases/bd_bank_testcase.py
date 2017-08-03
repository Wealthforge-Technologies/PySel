import unittest

from ..testpages.BDPages.bdhomepage import BDHomePage
from ..testcaseutilities.testinfo import TestInfo


class TestBDBank(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_BD_bank(self):

        bd_home_page = BDHomePage()
        bd_home_page.is_expected_landing_url()
        bd_home_page.menuDashboardBankSetup.click()



if __name__ == "__main__":
    unittest.main()
