import unittest

from ..testpages.OEPages.oeinvestmentpage import OEInvestmentPage
from ..testcaseutilities.testinfo import TestInfo


class TestInvestment(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):
        oe_investment_page = OEInvestmentPage()

        oe_investment_page.land()
        oe_investment_page.is_expected_landing_url()

        oe_investment_page.enter_info(self.lookup.testinfo["offering"],
                               self.lookup.testinfo["subDate"],
                               self.lookup.testinfo["investType"],
                               self.lookup.testinfo["payType"],
                               self.lookup.testinfo["invAmount"]
                               )

        oe_investment_page.clickForward()


if __name__ == "__main__":
    unittest.main()
