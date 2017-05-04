from selenium.webdriver.support.ui import WebDriverWait
from element import PageElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.abspath('../Utilities'))
from Utit import *

class BDLoginPage(BasePage):
    """QA login page action methods come here. I.e. https://qa1.wealthforge.org/login/#/"""
    url = "https://qa1.wealthforge.org/login/#/"
    email = PageElement(id_='username')
    password = PageElement(id_='password')
    btnLogin = PageElement(id_='btnLogin')

    def __init__(self, driver):
        self.driver = driver
        self.expected_landing_url = "https://qa1.wealthforge.org/login/#/"
        self.expected_title = "WF: Login"

    def is_expected_title(self):
        """Verifies that the hardcoded text "WF: Login" appears in page title"""
        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(self.expected_title))
        finally:
            assert self.expected_title in self.driver.title

    def is_expected_landing_url(self):
        """Verifies that the hardcoded text "WF: Login" appears in page title"""
        try:
            wait = WebDriverWait(self.driver(), 5).until(
                lambda wait: self.driver().current_url == self.expected_landing_url)
        finally:
            assert self.expected_landing_url in self.driver.current_url

    def land(self):
        self.driver.get(self.expected_landing_url)
        Utit.waitForAngular(self.driver)

    def login(self, username, password):
        self.email.send_keys(username)
        assert username in self.email.get_attribute("value")

        self.password.send_keys(password)
        assert password in self.password.get_attribute("value")

        self.btnLogin.click()
        Utit.waitForAngular(self.driver)
