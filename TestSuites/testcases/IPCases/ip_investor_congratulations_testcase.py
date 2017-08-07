import unittest

from TestSuites.testcases.testpages.IPPages.ipinvestorcongratulationspage import IPInvestorCongratulationsPage
from ..testcaseutilities.testinfo import TestInfo


class IPInvestorCongratulations(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):
        ip_payment_type_page = IPInvestorCongratulationsPage()
        ip_payment_type_page.is_expected_landing_url()
        ip_payment_type_page.linkReturnURL.click()


if __name__ == "__main__":
    unittest.main()
