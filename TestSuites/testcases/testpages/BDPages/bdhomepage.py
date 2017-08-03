from ..element import PageElement
from ..basepage import BasePage
from ..testpageutilities.waitforangular import waitForAngular


class BDHomePage(BasePage):
    menuDashboardAdmin = PageElement(id_='menuDashboardAdmin')  # BD/#/
    menuDashboardBankSetup = PageElement(id_='menuDashboardBankSetup')  # BD/#/
    menuDashboardOffering = PageElement(id_='menuDashboardOffering')  # BD/#/
    menuDashboardInvestor = PageElement(id_='menuDashboardInvestor')  # BD/#/
    menuDashboardInvestment = PageElement(id_='menuDashboardInvestment')  # BD/#/
    menuDashboardFinance = PageElement(id_='menuDashboardFinance')  # BD/#/
    menuDashboardIssuerDashboard = PageElement(id_='menuDashboardIssuerDashboard')  # BD/#/

    def __init__(self):
        BasePage.__init__(self,
                          url='/BD/#/',
                          title='WF: Broker Dealer')

    def clickAdminTab(self):
        # waitForAngular(self.driver)
        self.menuDashboardAdmin.click()

    def clickOfferingTab(self):
        waitForAngular(self.driver)
        self.menuDashboardOffering.click()
        waitForAngular(self.driver)
