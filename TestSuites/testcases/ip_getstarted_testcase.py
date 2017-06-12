import unittest

from TestSuites.testcases.testpages.ipgetstartedpage import IPGetStarted
from .testcaseutilities.testinfo import TestInfo


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_getstarted(self):

        ip_getstarted_page = IPGetStarted()
        # ip_getstarted_page.is_expected_landing_url()
        ip_getstarted_page.btnStart.click()


if __name__ == "__main__":
    unittest.main()
