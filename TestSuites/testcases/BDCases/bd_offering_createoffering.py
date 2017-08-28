import unittest

from ..testpages.BDPages.bdofferingtab_page import BDOfferingTabPage
from ..testpages.BDPages.bdofferingtab_info import BDOfferingTabInfo
from ..testpages.BDPages.bdofferingtab_documents import BDOfferingTabDocs
from ..testpages.BDPages.bdofferingtab_workflow import BDOfferingTabWork
from ..testpages.BDPages.bdhomepage import BDHomePage
from ..testcaseutilities.testinfo import TestInfo
import time

class TestBDOfferingCreateOffering(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()

    def test_bd_offering_create_offering(self):

        BDHomePage().clickOfferingTab()
        time.sleep(3)


        offeringPage = BDOfferingTabPage()
        offeringPage.load_treenodes()

        offeringPage.clickCreateOfferingByOrgId(offeringPage.getOrgIdByName('John ISS'))

        #====
        BDOfferingTabInfo().fill_offering_fields(self.lookup.testOfferInfo)
        BDOfferingTabInfo().fill_term_fields(self.lookup.testTermInfoDefaults, self.lookup.testTermInfoOther)
        BDOfferingTabInfo().submit()

        #TODO: verify info, edit info

        BDOfferingTabDocs().uploadDefaultDocs()
        BDOfferingTabDocs().save()

        offeringPage.load_treenodes()

        offeringPage.clickOfferingWorkflowByOffId(offeringPage.getOfferIdByName(self.lookup.testOfferInfo['offeringTitle']))

        BDOfferingTabWork().enterEscrowInfo(self.lookup.testOfferWorkflowInfo)

        BDOfferingTabWork().approveOffering()

        BDOfferingTabWork().save()

        while True:
            pass







if __name__ == "__main__":
    unittest.main()
