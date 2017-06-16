from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .element import PageElement
from .testpageutilities.waitforangular import waitForAngular
from .basepage import BasePage

class IPPaymentTypePage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/payment"""
    btnBack = PageElement(id_='Back')
    btnContinue = PageElement(id_='btnContinue')
    btnSaveForLater = PageElement(id_='btnSaveForLater')
    btnACH = PageElement(id_='divACH')
    btnCheck = PageElement(id_='divCheck')
    btnWire = PageElement(id_='divWire')
    btnIRA = PageElement(id_='divIRA')
    btnExchange = PageElement(id_='div1031_Exchange')
    acctTypes = PageElement(id_='ddlAccountTypes')
    ACHAcctName = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountName"())]')
    ACHAcctRouting = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountRouting"())]')
    ACHRoutingConf = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountRoutingConfirm"())]')
    ACHAcctNum = PageElement(xpath=“ // button[contains( @ ng - model = "account.ACHAccountNumber"())]“)
    ACHAcctNumConf = PageElement(xpath=“ // button[contains( @ ng - model = "account.ACHAccountNumberConfirm"())]“)



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

    def enter_info(self, ach, check, wire, ira, exchange, acctNme, acctTyp, acctRout, acctRoutConf, acctNum, acctNumConf):
        assert self.btnACH is not None
        self.btnACH.send_keys(ach)
        assert ach in self.btnACH.get_attribute("value")

        assert self.btnCheck is not None
        self.btnCheck.send_keys(check)
        assert check in self.btnCheck.get_attribute("value")

        assert self.btnWire is not None
        self.btnWire.send_keys(wire)
        assert wire in self.btnWire.get_attribute("value")

        assert self.btnIRA is not None
        self.btnIRA.send_keys(ira)
        assert ira in self.btnIRA.get_attribute("value")

        assert self.btnExchange is not None
        self.btnExchange.send_keys(exchange)
        assert exchange in self.btnExchange.get_attribute("value")

        assert self.acctName is not None
        self.acctName.sendKeys(acctNme)
        assert acctNme in self.acctName.get_attribute("value")

        assert self.acctTypes is not None
        self.acctTypes.sendKeys(acctTyp)
        assert acctTyp in self.acctTypes.get_attribute("value")

        assert self.acctRouting is not None
        self.acctRouting.sendKeys(acctRout)
        assert acctRout in self.acctRouting.get_attribute("value")

        assert self.acctRoutingConf is not None
        self.acctRoutingConf.sendKeys(acctRoutConf)
        assert acctRoutConf in self.acctRoutingConf.get_attribute("value")

        assert self.acctNumber is not None
        self.acctNumber.sendKeys(acctNum)
        assert acctNum in self.acctNumber.get_attribute("value")

        assert self.acctNumberConf is not None
        self.acctNumberConf.sendKeys(acctNumConf)
        assert acctNumConf in self.acctNumberConf.get_attribute("value")


    def land(self):
        self.driver.get(self.expected_landing_url)


        def clickContinue(self):
            self.btnContinue.click()
            waitForAngular(self.driver)

        def clickACH(self):
            self.btnACH.click()
            waitForAngular(self.driver)

