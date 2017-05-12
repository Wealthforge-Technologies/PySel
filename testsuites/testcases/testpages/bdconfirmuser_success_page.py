from selenium.webdriver.support.ui import WebDriverWait
from .element import PageElement
from .basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .testpageutilities.waitforangular import waitForAngular
import time


class BDConfirmUserSuccessPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/rad
    submit_button = PageElement(id_='btnReturnToLogin')

    def __init__(self, driver):
        self.driver = driver
        self.expected_title = "WF: Login"

    def is_expected_title(self):
        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(self.expected_title))
        finally:
            assert self.expected_title in self.driver.title
        waitForAngular(self.driver)

    def submit(self):
        assert self.submit_button is not None
        self.submit_button.click()
        waitForAngular(self.driver)
