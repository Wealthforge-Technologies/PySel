from selenium.webdriver.support.ui import WebDriverWait
from element import PageElement
from selenium import webdriver
from selenium.webdriver.common.by import By

class BDHomePage(BasePage):
    # https://qa1.wealthforge.org/BD/#/
    menuDashboardAdmin = PageElement(id_='menuDashboardAdmin')  # BD/#/
    menuDashboardBankSetup = PageElement(id_='menuDashboardBankSetup')  # BD/#/
    menuDashboardOffering = PageElement(id_='menuDashboardOffering')  # BD/#/
    menuDashboardInvestor = PageElement(id_='menuDashboardInvestor')  # BD/#/
    menuDashboardInvestment = PageElement(id_='menuDashboardInvestment')  # BD/#/
    menuDashboardInvestor = PageElement(id_='menuDashboardInvestor')  # BD/#/
    menuDashboardFinance = PageElement(id_='menuDashboardFinance')  # BD/#/
    menuDashboardIssuerDashboard = PageElement(id_='menuDashboardIssuerDashboard')  # BD/#/

    def __init__(self, driver):
        self.driver = driver
        self.expected_landing_url = "https://qa1.wealthforge.org/BD/#/"
        self.expected_title = "WF: Broker Dealer"

    def is_expected_title(self):
        """Verifies that the hardcoded text "WF: Login" appears in page title"""
        assert self.expected_title in self.driver.title

    def is_expected_landing_url(self):
        """Verifies that the hardcoded text "WF: Login" appears in page title"""
        assert self.expected_landing_url in self.driver.current_url

    def land(self):
        self.driver.get(self.expected_landing_url)
