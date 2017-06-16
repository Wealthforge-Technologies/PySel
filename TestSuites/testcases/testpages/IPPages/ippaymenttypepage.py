from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from selenium.webdriver.support.ui import Select

class IPPaymentTypePage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/payment"""
    btnACH = PageElement(id_='divACH')
    btnCheck = PageElement(id_='divCheck')
    btnWire = PageElement(id_='divWire')
    btnIRA = PageElement(id_='divIRA')
    btnExchange = PageElement(id_='div1031_Exchange')

    achAcctName = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountName"())]')
    achAcctTypes = PageElement(id_='ddlAccountTypes')
    achAcctRouting = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountRouting"())]')
    achAcctRoutingConf = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountRoutingConfirm"())]')
    achAcctNum = PageElement(xpath='//button[contains(@ ng-model="account.ACHAccountNumber"())]')
    achAcctNumConf = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountNumberConfirm"())]')

    #TODO: Existing ACH

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/payment',
                          title='WF: Investor Platform')

    def selectAch(self,achName, achType, achRout, achNumb):
        assert self.btnACH is not None
        self.btnACH.click()
        waitForAngular(self.driver)

        assert self.achAcctName is not None
        assert self.achAcctTypes is not None
        assert self.achAcctRouting is not None
        assert self.achAcctRoutingConf is not None
        assert self.achAcctNum is not None
        assert self.achAcctNumConf is not None

        self.achAcctName.send_keys(achName)
        Select(self.achAcctTypes).select_by_visible_text(achType)
        self.achAcctRouting.send_keys(achRout)
        self.achAcctRoutingConf.send_keys(achRout)
        self.achAcctNum.send_keys(achNumb)
        self.achAcctNumConf.send_keys(achNumb)

        assert achName is self.achAcctName.get_attribute("value")
        assert achType is self.achAcctTypes.get_attribute("value")
        assert achRout is self.achAcctRouting.get_attribute("value")
        assert achRout is self.achAcctRoutingConf.get_attribute("value")
        assert achNumb is self.achAcctNum.get_attribute("value")
        assert achNumb is self.achAcctNumConf.get_attribute("value")

    def selectCheck(self):
        assert self.btnCheck is not None
        self.btnCheck.click()
        waitForAngular(self.driver)

    def selectIra(self):
        assert self.btnIRA is not None
        self.btnIRA.click()
        waitForAngular(self.driver)

    def selectWire(self):
        assert self.btnWire is not None
        self.btnWire.click()
        waitForAngular(self.driver)

    def selectExchange(self):
        assert self.btnExchange is not None
        self.btnExchange.click()
        waitForAngular(self.driver)


    # def enter_info(self, ach, check, wire, ira, exchange):
    #     assert self.btnACH is not None
    #     self.btnACH.send_keys(ach)
    #     assert ach in self.btnACH.get_attribute("value")
    #
    #     assert self.btnCheck is not None
    #     self.btnCheck.send_keys(check)
    #     assert check in self.btnCheck.get_attribute("value")
    #
    #     assert self.btnWire is not None
    #     self.btnWire.send_keys(wire)
    #     assert wire in self.btnWire.get_attribute("value")
    #
    #     assert self.btnIRA is not None
    #     self.btnIRA.send_keys(ira)
    #     assert ira in self.btnIRA.get_attribute("value")
    #
    #     assert self.btnExchange is not None
    #     self.btnExchange.send_keys(exchange)
    #     assert exchange in self.btnExchange.get_attribute("value")
    #
    #     assert self.acctTypes is not None
    #     self.acctTypes.sendKeys(acctTyp)
    #     assert acctTyp in self.acctTypes.get_attribute("value")


