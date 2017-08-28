import unittest

from ..testpages.OEPages.oeloginpage import OELoginPage
from ..testcaseutilities.testinfo import TestInfo


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):
        oe_login_page = OELoginPage()

        oe_login_page.land()
        oe_login_page.is_expected_landing_url()

        oe_login_page.clickLogin()


if __name__ == "__main__":
    unittest.main()
