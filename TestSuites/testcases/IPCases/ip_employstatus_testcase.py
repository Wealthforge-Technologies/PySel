import unittest

from ..testpages.IPPages.ipemploystatuspage import IPEmploymentStatusPage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral

class TestIPEmploymentStatus(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):

        ip_employstatus_page = IPEmploymentStatusPage()
        ip_employstatus_page.is_expected_landing_url()



        ip_employstatus_page.enter_info(self.lookup.testinfo['Employment Status'],
                                        self.lookup.testinfo['otherOpport'],
                                        self.lookup.testinfo['rbFINRA'],
                                        self.lookup.testinfo['CRD Number'],
                                        )

        IPGeneral().clickContinue()

if __name__ == "__main__":
    unittest.main()
