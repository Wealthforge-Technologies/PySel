from selenium.webdriver.support.ui import WebDriverWait
from element import PageElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """QA login page action methods come here. I.e. https://qa1.wealthforge.org/login/#/"""
    url = "https://qa1.wealthforge.org/login/#/"
    email = PageElement(id_='username')
    password = PageElement(id_='password')

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        """Verifies that the hardcoded text "WF: Login" appears in page title"""
        assert "WF: Login" in self.driver.title

    def submit(self):
        try:
            wait = WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.find_element_by_id('btnLogin'))
        finally:
            self.driver.find_element_by_id('btnLogin').click()


class BDPage(BasePage):
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

    def is_title_matches(self):
        """Verifies that the hardcoded text "WF: Login" appears in page title"""
        assert "WF: Login" in self.driver.title


class BDRadPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/rad
    search = PageElement(id_='search')
    hamburger = PageElement(id_='appDrawerToggle')
    topRightDropdown = PageElement(css='#bs-example-navbar-collapse-1 > ul > li > a')

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        """Verifies that the hardcoded text "WF: Login" appears in page title"""
        assert "WF: Login" in self.driver.title
