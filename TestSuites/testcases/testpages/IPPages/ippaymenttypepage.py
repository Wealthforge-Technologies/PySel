from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

class IPPaymentTypePage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/payment"""
    btnACH = PageElement(id_='divACH')
    btnCheck = PageElement(id_='divCheck')
    btnWire = PageElement(id_='divWire')
    btnIRA = PageElement(id_='divIRA')
    btnExchange = PageElement(id_='div1031_Exchange')
    acctTypes = PageElement(id_='ddlAccountTypes')
    ACHAcctName = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountName"())]')
    ACHAcctRouting = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountRouting"())]')
    ACHRoutingConf = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountRoutingConfirm"())]')
    ACHAcctNum = PageElement(xpath='//button[contains(@ ng-model="account.ACHAccountNumber"())]')
    ACHAcctNumConf = PageElement(xpath='//button[contains(@ng-model="account.ACHAccountNumberConfirm"())]')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/payment',
                          title='WF: Investor Platform')

    # def selectACH(self,achName, achType, achRout, achNumb):
        #TODO:

    def selectCheck(self):
        pass


    def enter_info(self, ach, check, wire, ira, exchange):
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

        assert self.acctTypes is not None
        self.acctTypes.sendKeys(acctTyp)
        assert acctTyp in self.acctTypes.get_attribute("value")


