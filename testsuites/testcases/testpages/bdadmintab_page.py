from selenium.webdriver.support.ui import WebDriverWait
from element import PageElement
from selenium import webdriver
from selenium.webdriver.common.by import By

class BDAdminTabPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/rad
    search = PageElement(id_='search')
    hamburger = PageElement(id_='appDrawerToggle')
    topRightDropdown = PageElement(css='#bs-example-navbar-collapse-1 > ul > li > a')

    def __init__(self, driver):
        self.driver = driver
        self.expected_landing_url = "https://qa1.wealthforge.org/BD/#/rad"
        self.expected_title = "WF: Broker Dealer"

    def is_expected_title(self):
        """Verifies that the hardcoded text "WF: Login" appears in page title"""
        assert self.expected_title in self.driver.title

    def is_expected_landing_url(self):
        """Verifies that the hardcoded text "WF: Login" appears in page title"""
        assert self.expected_landing_url in self.driver.current_url

    def land(self):
        self.driver.get(self.expected_landing_url
