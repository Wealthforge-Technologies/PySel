from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver


class BDLoginPage(BasePage):
    email = PageElement(id_='username')
    password = PageElement(id_='password')
    btnLogin = PageElement(id_='btnLogin')

    def __init__(self):
        BasePage.__init__(self,
                          url='/login/#/',
                          title='WF: Login')


    # def __init__(self):
    #     self.driver = getOrCreateWebdriver()
    #     self.expected_landing_url = "https://qa1.wealthforge.org/login/#/"
    #     self.expected_title = "WF: Login"
    #
    # def is_expected_title(self):
    #     """Verifies that the hardcoded text "WF: Login" appears in page title"""
    #     try:
    #         wait = WebDriverWait(self.driver, 5).until(
    #             EC.title_contains(self.expected_title))
    #     finally:
    #         assert self.expected_title in self.driver.title
    #     waitForAngular(self.driver)
    #
    #
    # def is_expected_landing_url(self):
    #     """Verifies that the hardcoded text "WF: Login" appears in page title"""
    #     try:
    #         wait = WebDriverWait(self.driver, 5).until(
    #             lambda wait: self.driver.current_url == self.expected_landing_url)
    #     finally:
    #         assert self.expected_landing_url in self.driver.current_url
    #     waitForAngular(self.driver)
    #
    # def land(self):
    #     self.driver.get(self.expected_landing_url)

    #This method is a form submit for the BD login screen which leads to bdhomepage
    def login(self, username, password):
        self.email.send_keys(username)
        assert username in self.email.get_attribute("value")

        self.password.send_keys(password)
        assert password in self.password.get_attribute("value")

        self.btnLogin.click()
        waitForAngular(self.driver)
