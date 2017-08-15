import unittest

from ..testpages.IPPages.ipgetstartedpage import IPGetStarted
from ..testcaseutilities.testinfo import TestInfo


class GetStartedStartOver(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_getstarted(self):

        ip_getstarted_page = IPGetStarted()
        # ip_getstarted_page.is_expected_landing_url()
        # ip_getstarted_page.btnStart.click()
        ip_getstarted_page.clickStartOrStartOver()

if __name__ == "__main__":
    unittest.main()
