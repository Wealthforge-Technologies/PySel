from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

class IPDocusignPage(BasePage):
    chkboxDisclosure = PageElement(id_='disclosureAccepted')
    btnDocusignContinue = PageElement(id_='action-bar-btn-continue')
    btnNext = PageElement(id_='navigate-btn')
    iframe = PageElement(id_='signing')
    btnSign = PageElement(css='[id^=tab-form-element-]')  # [id^=__id__] means id starts with
    modalAdoptAndSign = PageElement(id_='adopt-dialog')
    btnAdoptAndSign = PageElement(xpath='//*[@id="adopt-dialog"]/div/div[3]/button[1]')
    btnFinish = PageElement(id_='action-bar-btn-finish')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/document/upload',
                          title='WF: Investor Platform')

    def switchToIframe(self):
        self.driver.switch_to.frame(self.iframe)

    def ifr(self):
        print(self.driver.find_element_by_xpath('html/body').get_attribute('value'))