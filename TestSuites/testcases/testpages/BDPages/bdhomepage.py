from selenium.webdriver.support.ui import WebDriverWait
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver


class BDHomePage(BasePage):
    # https://qa1.wealthforge.org/BD/#/
    menuDashboardAdmin = PageElement(id_='menuDashboardAdmin')  # BD/#/
    menuDashboardBankSetup = PageElement(id_='menuDashboardBankSetup')  # BD/#/
    menuDashboardOffering = PageElement(id_='menuDashboardOffering')  # BD/#/
    menuDashboardInvestor = PageElement(id_='menuDashboardInvestor')  # BD/#/
    menuDashboardInvestment = PageElement(id_='menuDashboardInvestment')  # BD/#/
    menuDashboardFinance = PageElement(id_='menuDashboardFinance')  # BD/#/
    menuDashboardIssuerDashboard = PageElement(id_='menuDashboardIssuerDashboard')  # BD/#/


    def __init__(self):
        self.driver = getOrCreateWebdriver()
        self.expected_landing_url = "https://qa1.wealthforge.org/BD/#/"
        self.expected_title = "WF: Broker Dealer"

    def is_expected_title(self):
        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(self.expected_title))
        finally:
            assert self.expected_title in self.driver.title
        waitForAngular(self.driver)

    def is_expected_landing_url(self):
        try:
            wait = WebDriverWait(self.driver, 5).until(
                lambda wait: self.driver.current_url == self.expected_landing_url)
        finally:
            assert self.expected_landing_url in self.driver.current_url
        waitForAngular(self.driver)


    def land(self):
        self.driver.get(self.expected_landing_url)
        waitForAngular(self.driver)
