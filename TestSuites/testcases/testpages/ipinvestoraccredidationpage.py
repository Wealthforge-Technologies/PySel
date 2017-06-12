from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .element import PageElement
from .testpageutilities.waitforangular import waitForAngular
from .basepage import BasePage
from .testpageutilities import getOrCreateWebdriver


class IPInvestorAccredidationPage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/ind/registration"""
    btnBack = PageElement(id_='Back')
    btnContinue = PageElement(id_='btnContinue')
    btnNetWorth = PageElement(id_='divTypeNet_Worth')
    btnIncome = PageElement(id_='divTypeIncome')
    btnNotAccred = PageElement(id_='divTypeNotAccredited')

    def __init__(self):
        self.driver = getOrCreateWebdriver()
        self.expected_landing_url = "https://qa1.wealthforge.org/IP/#/ind/registration"
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

    def enter_info(self, net, income, notAcc):
        assert self.btnNetWorth is not None
        self.btnNetWorth.send_keys(net)
        assert net in self.btnNetWorth.get_attribute("value")

        assert self.btnIncome is not None
        self.btnIncome.send_keys(income)
        assert income in self.btnIncome.get_attribute("value")

        assert self.btnNotAccred is not None
        self.btnNotAccred.send_keys(notAcc)
        assert notAcc in self.btnNotAccred.get_attribute("value")


    def land(self):
        self.driver.get(self.expected_landing_url)


        def clickContinue(self):
            self.btnContinue.click()
            waitForAngular(self.driver)

        def clickNetWorth(self):
            self.divTypeNet_Worth.click()
            waitForAngular(self.driver)

