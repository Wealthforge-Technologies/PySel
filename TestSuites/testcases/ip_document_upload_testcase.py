import unittest
from TestSuites.testcases.testpages.ipdocumentuploadpage import IPDocumentUploadPage
from .testcaseutilities.testinfo import TestInfo


class TestDocumentUploadPage(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):

        ip_document_upload_page = IPDocumentUploadPage()
        ip_document_upload_page.is_expected_landing_url()

        ip_document_upload_page.fileBox.click()
        ip_document_upload_page.btnContinue.click()



if __name__ == "__main__":
    unittest.main()
