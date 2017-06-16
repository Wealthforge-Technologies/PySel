import unittest

from TestSuites.testcases.testpages import IPInvestorCongratulationsPage
from .testcaseutilities.testinfo import TestInfo


class IPInvestorCongratulationsPage(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        ip_payment_type_page = IPInvestorCongratulationsPage(self.driver)
        ip_payment_type_page.is_expected_landing_url()
        ip_payment_type_page.linkReturnURL.click()


if __name__ == "__main__":
    unittest.main()
