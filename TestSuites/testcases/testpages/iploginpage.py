from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .element import PageElement
from .testpageutilities.waitforangular import waitForAngular
from .basepage import BasePage

class IPLoginPage(BasePage):
    """QA login page action methods come here. I.e. https://qa1.wealthforge.org/login/#/"""
    url = "https://qa1.wealthforge.org/IP/#/login/2eb2d7ff-1fa9-4f72-8dd5-e1527bf58cb3"
    email = PageElement(id_='username')
    password = PageElement(id_='password')
    btnLogin = PageElement(id_='btnLogin')
    btnSignUp = PageElement(id_='btnSignUp')
    lnkForgotPassword = PageElement(id_='linkForgotPassword')

    def __init__(self, driver):
        self.driver = driver
        self.expected_landing_url = "https://qa1.wealthforge.org/IP/#/login/2eb2d7ff-1fa9-4f72-8dd5-e1527bf58cb3"
        self.expected_title = "WF: Investor Platform"

    def is_expected_title(self):
        """Verifies that the hardcoded text "WF: Investor Platform" appears in page title"""
        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(self.expected_title))
        finally:
            assert self.expected_title in self.driver.title
        waitForAngular(self.driver)


    def is_expected_landing_url(self):
        """Verifies that the hardcoded text "WF: Investor Platform" appears in page title"""
        try:
            wait = WebDriverWait(self.driver, 5).until(
                lambda wait: self.driver.current_url == self.expected_landing_url)
        finally:
            assert self.expected_landing_url in self.driver.current_url
        waitForAngular(self.driver)

    def land(self):
        self.driver.get(self.expected_landing_url)

    #This method is a form submit for the IP login screen which leads to iphomepage
    def login(self, username, password):
        self.email.send_keys(username)
        assert username in self.email.get_attribute("value")

        self.password.send_keys(password)
        assert password in self.password.get_attribute("value")

        self.btnLogin.click()
        waitForAngular(self.driver)