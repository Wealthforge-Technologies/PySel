import unittest
import time

from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipdocusignpage import IPDocusignPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_docusign_firsttime(self):

        docusign = IPDocusignPage()

        time.sleep(10)

        docusign.switchToIframe()
        time.sleep(1)
        docusign.ifr()

        docusign.chkboxDisclosure.click()
        time.sleep(1)

        docusign.btnDocusignContinue.click()
        time.sleep(1)
        docusign.btnNext.click()
        time.sleep(1)
        docusign.btnSign.click()
        time.sleep(1)
        time.sleep(1)



if __name__ == "__main__":
    unittest.main()
