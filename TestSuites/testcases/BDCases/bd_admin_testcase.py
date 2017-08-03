import unittest
from ..testcaseutilities.testinfo import TestInfo
# from TestSuites.testcases.testpages.BDPages.bdhomepage import BDHomePage
from TestSuites.testcases.testpages.BDPages.bdadmintab_page import BDAdminTabPage


class TestBDAdmin(unittest.TestCase):

    def test_BD_admin(self):

        admin = BDAdminTabPage()
        admin.clickAdmin()

        # bd_home_page = BDHomePage()
        # # bd_home_page.is_expected_landing_url()
        # #
        # bd_home_page.clickAdminTab()
        # # bd_home_page.menuDashboardAdmin.click()


if __name__ == "__main__":
    unittest.main()
