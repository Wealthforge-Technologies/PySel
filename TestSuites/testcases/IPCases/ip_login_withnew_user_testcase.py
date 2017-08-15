import unittest

from ..testpages.IPPages.iploginpage import IPLoginPage
from ..testcaseutilities.testinfo import TestInfo


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):
        ip_login_page = IPLoginPage()

        ip_login_page.is_expected_landing_url()

        ip_login_page.login(self.lookup.testinfo["email"],
                            self.lookup.testinfo["username"])
        print(type(ip_login_page.btnLogin))


if __name__ == "__main__":
    unittest.main()
