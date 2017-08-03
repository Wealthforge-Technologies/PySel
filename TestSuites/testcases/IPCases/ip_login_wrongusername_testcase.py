import unittest

from ..testpages.IPPages.iploginpage import IPLoginPage
from ..testcaseutilities.testinfo import TestInfo


class TestLoginWrongUsername(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_login_page = IPLoginPage()

        ip_login_page.land()
        ip_login_page.is_expected_landing_url()
        ip_login_page.login(self.lookup.testinfo["IP.emailWrong"],self.lookup.testinfo["IP.password"])



if __name__ == "__main__":
    unittest.main()
