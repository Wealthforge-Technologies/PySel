from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

class IPDocumentUploadPage(BasePage):
    uploadButton = PageElement(id_='fileBox')
    chkBoxProceed = PageElement(id_='chkProceed')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/document/upload',
                          title='WF: Investor Platform')


    def clickUploadButton(self):
        self.uploadButton.click()
        waitForAngular(self.driver)

    def clickCheckBox(self):
        self.chkBoxProceed.click()
        waitForAngular(self.driver)
