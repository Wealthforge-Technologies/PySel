from selenium.webdriver.support.ui import WebDriverWait
from .element import PageElement
from .basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .testpageutilities.waitforangular import waitForAngular
import time
from .basepage import BasePage
from .testpageutilities import getOrCreateWebdriver


class BDConfirmUserPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/rad
    password = PageElement(id_='username')
    confirm = PageElement(id_='password')
    submit_button = PageElement(id_='btnSetPassword')

    def __init__(self, expected_reset_url):
        self.driver = getOrCreateWebdriver()
        self.expected_title = "WF: Login"
        self.expected_landing_url = expected_reset_url

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

    def enter_password(self, newpassword):
        assert self.password is not None
        self.password.send_keys(newpassword)
        assert newpassword in self.password.get_attribute("value")

        assert self.confirm is not None
        self.confirm.send_keys(newpassword)
        assert newpassword in self.confirm.get_attribute("value")
        waitForAngular(self.driver)

    def submit(self):
        assert self.submit_button is not None
        self.submit_button.click()
        waitForAngular(self.driver)
