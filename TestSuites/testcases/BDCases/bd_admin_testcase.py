import unittest

from TestSuites.testcases.testpages.BDPages.bdhomepage import BDHomePage
from ..testcaseutilities.testinfo import TestInfo


class TestBDAdmin(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_BD_admin(self):

        bd_home_page = BDHomePage()
        bd_home_page.is_expected_landing_url()
        bd_home_page.menuDashboardAdmin.click()



if __name__ == "__main__":
    unittest.main()
