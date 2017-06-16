from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .element import PageElement
from .testpageutilities.waitforangular import waitForAngular
from .basepage import BasePage

class IPInvestorConfirmationPage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/payment"""
    chkBoxAffirmCC = PageElement(id_='chkAffirmCreditCheck')
    chkBoxAffirmTC = PageElement(id_='chkAffirmTermsAndConditions')
    btnBack = PageElement(id_='Back')
    btnContinue = PageElement(id_='btnContinue')


    def __init__(self, driver):
        self.driver = driver
        self.expected_landing_url = "https://qa1.wealthforge.org/IP/#/payment"
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


        def clickContinue(self):
            self.btnContinue.click()
            waitForAngular(self.driver)


