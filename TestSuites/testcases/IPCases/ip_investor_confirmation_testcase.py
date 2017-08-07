import unittest

from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipinvestmentconfirmationpage import IPInvestorConfirmationPage
from testutilities import Settings
from ..testpages.IPPages.ipgeneralpage import IPGeneral


class IPInvestorConfirmationCase(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()

    def test_confirm(self):
        confirm = IPInvestorConfirmationPage()
        confirm.is_expected_landing_url()

        confirm.chkBoxAffirmCC.click()
        confirm.chkBoxAffirmTC.click()

        IPGeneral().clickContinue()


if __name__ == "__main__":
    unittest.main()
