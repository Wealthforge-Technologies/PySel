import unittest
import time

from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipdocusignpage import IPDocusignPage
from testutilities import Settings

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_docusign_firsttime(self):
        Settings.ISANGULAR = False

        docusign = IPDocusignPage()

        docusign.switchToIframe()
        time.sleep(1)


        if docusign.modalAdoptAndSign is not None or docusign.chkboxDisclosure.is_displayed():
            docusign.chkboxDisclosure.click()

        docusign.btnDocusignContinue.click()
        time.sleep(1)

        docusign.btnNext.click()
        time.sleep(1)

        docusign.btnSign.click()
        time.sleep(1)

        # If the investor is going through and signing for the second time with the same Name and Email, Docusign will
        # not require the user to check the signature again.
        if docusign.modalAdoptAndSign is not None:
            docusign.btnAdoptAndSign.click()
            time.sleep(1)


        docusign.btnFinish.click()
        time.sleep(1)


        Settings.ISANGULAR = True



if __name__ == "__main__":
    unittest.main()
