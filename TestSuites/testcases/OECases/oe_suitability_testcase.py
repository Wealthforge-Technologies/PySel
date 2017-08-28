import unittest

from ..testpages.OEPages.oesuitabilitypage import OESuitabilityPage
from ..testcaseutilities.testinfo import TestInfo


class TestSuitability(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):
        oe_suitability_page = OESuitabilityPage()

        oe_suitability_page.land()
        oe_suitability_page.is_expected_landing_url()

        oe_suitability_page.clickAnswerSuitabilityQs()

        oe_suitability_page.enter_info(self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""],
                               self.lookup.testinfo[""]
                               )

        oe_suitability_page.clickForward()


if __name__ == "__main__":
    unittest.main()
