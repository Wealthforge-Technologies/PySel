from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

class IPGeneral(BasePage):
    btnContinue = PageElement(id_='btnContinue')
    btnBack = PageElement(id_='btnBack') #TODO:
    btnLogout = PageElement(id_='linkLogout')



    def __init__(self):
        BasePage.__init__(self)

    def clickContinue(self):
        self.btnContinue.click()
        waitForAngular(self.driver)

    def clickBack(self):
        self.btnBack.click()
        waitForAngular(self.driver)

    def logout(self):
        self.btnLogout.click()
        waitForAngular(self.driver)

