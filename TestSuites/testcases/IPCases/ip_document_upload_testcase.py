import unittest
from ..testpages.IPPages.ipdocumentuploadpage import IPDocumentUploadPage
from ..testcaseutilities.testinfo import TestInfo
from ..testpages.IPPages.ipgeneralpage import IPGeneral

class TestDocumentUploadPage(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()

    def test_login(self):

        ip_document_upload_page = IPDocumentUploadPage()
        ip_document_upload_page.is_expected_landing_url()

        #TODO: upload a document

        ip_document_upload_page.clickCheckBox()

        IPGeneral().clickContinue()


if __name__ == "__main__":
    unittest.main()
