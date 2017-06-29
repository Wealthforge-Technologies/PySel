from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

class IPInvestorCongratulationsPage(BasePage):
    btnReturn = PageElement(id_='linkReturnURL')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/ind/complete',
                          title='WF: Investor Platform')

    def clickReturn(self):
        self.btnReturn.click()
        waitForAngular(self.driver)
