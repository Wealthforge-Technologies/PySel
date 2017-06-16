import unittest
from ..testpages.IPPages.ippaymenttypepage import IPPaymentTypePage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral


class TestPaymentTypePage(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        pay = IPPaymentTypePage()
        pay.is_expected_landing_url()

        pay.selectCheck()

        IPGeneral().clickContinue()


if __name__ == "__main__":
    unittest.main()
