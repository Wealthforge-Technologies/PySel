from .element import PageElement
from .testpageutilities.waitforangular import waitForAngular
from .basepage import BasePage

class IPIndividualCongratualtionsPage(BasePage):
    btnReturn = PageElement(id_='linkReturnURL')


        def clickReturn(self):
            self.btnReturn.click()
            waitForAngular(self.driver)
