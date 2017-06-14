import unittest

from ..testpages.IPPages.ippaymenttypepage import IPPaymentTypePage
from ..testcaseutilities.testinfo import TestInfo


class TestPaymentTypePage(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_payment_type_page = IPPaymentTypePage()
        ip_payment_type_page.is_expected_landing_url()
        ip_payment_type_page.divACH.click()

        ip_payment_type_page.regInfo(self.lookup.testinfo["sq-10"])

        ip_payment_type_page.btnContinue.click()




if __name__ == "__main__":
    unittest.main()
