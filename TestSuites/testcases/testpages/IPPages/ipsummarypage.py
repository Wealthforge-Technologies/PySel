from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver

class IPSummaryPage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/summary"""
    btnInvestAmount = PageElement(id_='investAmount')
    btnQuickContinue = PageElement(id_='btnQuickContinue')
    header = PageElement(id_='hHeadLine')
    offerTab = PageElement(name='offerTab')
    filesTab = PageElement(name='filesTab')
    invAmount = PageElement(id_='invAmnt')
    invAmountWrong = PageElement(id_='invAmnt')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/summary',
                          title='WF: Investor Platform')

    def enter_info(self, invAmtWrong):
        assert self.invAmountWrong is not None
        self.invAmountWrong.send_keys(invAmtWrong)
        assert invAmtWrong in self.invAmountWrong.get_attribute("value")

    #This method is a form submit for the IP Summary Page
    def clickContinue(self):

        self.btnContinue.click()
        waitForAngular(self.driver)

    def invest(self, amount):
        assert self.invAmountWrong is not None
        self.invAmountWrong.send_keys(amount)
        #TODO: check the text below the field

        self.btnInvestAmount.click()
        waitForAngular(self.driver)

