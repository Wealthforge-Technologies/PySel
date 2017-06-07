from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from .element import PageElement
from .testpageutilities.waitforangular import waitForAngular
from .basepage import BasePage
from .testpageutilities import getOrCreateWebdriver

class BDBankTabPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/banks
    create_bank_btn = PageElement(xpath="//nav[contains(@label,'Create Bank')]")


    def __init__(self):
        self.driver = getOrCreateWebdriver
        self.expected_landing_url = "https://qa1.wealthforge.org/BD/#/banks"
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
