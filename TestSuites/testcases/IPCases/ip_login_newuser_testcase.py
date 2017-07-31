import unittest

from ..testpages.IPPages.iploginpage import IPLoginPage
from ..testcaseutilities.testinfo import TestInfo


class TestLoginNewUser(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_login_page = IPLoginPage()

        ip_login_page.land()
        ip_login_page.btnSignUp()



if __name__ == "__main__":
    unittest.main()
