import unittest

from ..testpages.BDPages.bdloginpage import BDLoginPage
from ..testcaseutilities.testinfo import TestInfo


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        bd_login_page = BDLoginPage()

        bd_login_page.land()
        bd_login_page.is_expected_landing_url()

        bd_login_page.login(self.lookup.testinfo["CCO.email"],
                            self.lookup.testinfo["CCO.password"])



if __name__ == "__main__":
    unittest.main()
