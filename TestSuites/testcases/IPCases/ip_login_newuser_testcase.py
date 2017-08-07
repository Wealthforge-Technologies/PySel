import unittest

from ..testpages.IPPages.iploginpage import IPLoginPage
from ..testcaseutilities.testinfo import TestInfo


class TestLoginNewUser(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_click_signup(self):
        ip_login_page = IPLoginPage()

        ip_login_page.land()
        ip_login_page.clickSignup()



if __name__ == "__main__":
    unittest.main()
