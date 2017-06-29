from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

class IPGettingToKnowYou(BasePage):
    gtkyAddress = PageElement(id_='address')
    gtkyAddressCont = PageElement(id_='addressCont')
    gtkyCity = PageElement(id_='city')
    gtkyState = PageElement(id_='stateDrop')
    gtkyZipCode = PageElement(id_='zip')
    gtkyPhoneNum = PageElement(id_='phone')
    chkBoxUserAgree = PageElement(id_='userAgree')
    btnContinue = PageElement(xpath='//*[@id="506bsignupForm"]/div[2]/div[2]/input')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/ind/investorInf',
                          title='WF: Investor Platform')

    def chkBoxUserAgree(self):
        self.chkBoxUserAgree.click()
        waitForAngular(self.driver)

    def clickContinue(self):
        self.btnContinue.click()
        waitForAngular(self.driver)


