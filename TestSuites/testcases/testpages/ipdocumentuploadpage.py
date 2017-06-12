from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .element import PageElement
from .testpageutilities.waitforangular import waitForAngular
from .basepage import BasePage
from .testpageutilities import getOrCreateWebdriver

class IPDocumentUploadPage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/document/upload"""
    btnBack = PageElement(id_='Back')
    btnContinue = PageElement(id_='btnContinue')
    btnFileBox = PageElement(id_='fileBox')
    chkBoxProceed = PageElement(id_='chkProceed')
    btnSaveForLater = PageElement(id_='btnSaveForLater')


    def __init__(self):
        self.driver = getOrCreateWebdriver()
        self.expected_landing_url = "https://qa1.wealthforge.org/IP/#/document/upload"
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

    def enter_info(self, file, check, save):
        assert self.btnFileBox is not None
        self.btnFileBox.send_keys(file)
        assert file in self.btnFileBox.get_attribute("value")

        assert self.chkBoxPro is not None
        self.chkBoxPro.send_keys(check)
        assert check in self.chkBoxPro.get_attribute("value")

        assert self.saveForLtr is not None
        self.saveForLtr.send_keys(save)
        assert save in self.saveForLtr.get_attribute("value")

    def land(self):
        self.driver.get(self.expected_landing_url)


        def clickContinue(self):
            self.btnContinue.click()
            waitForAngular(self.driver)

        def clickFileBox(self):
            self.fileBox.click()
            waitForAngular(self.driver)

        def clickCheckBox(self):
            self.chkProceed.click()
            waitForAngular(self.driver)

        def clickSaveForLater(self):
            self.btnSaveForLater.click()
            waitForAngular(self.driver)

