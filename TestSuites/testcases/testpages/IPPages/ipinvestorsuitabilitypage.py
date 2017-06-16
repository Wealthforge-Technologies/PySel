from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver

class IPInvestorSuitabilityPage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/ind/registration"""
    primInvObj = PageElement(id_='sq-10')
    relInvExp = PageElement(id_='sq-20')
    wilAccptRisk = PageElement(id_='sq-30')
    maxInvHorizon = PageElement(id_='sq-40')
    currentPortInvEq = PageElement(id_='sq-50')
    currentPortInvBond = PageElement(id_='sq-60')
    currentPortInvRE = PageElement(id_='sq-70')
    currentPortInvOther = PageElement(id_='sq-80')
    immedLiqWorth = PageElement(id_='sq-90')
    annualLivExp = PageElement(id_='sq-100')
    margPerTaxRt = PageElement(id_='sq-110')
    iUnderstand = PageElement(id_='sq-120')
    iHaveConduct = PageElement(id_='sq-130')
    invAmount = PageElement(id_='invAmnt')
    btnInvAmt = PageElement(id_='investAmount')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/suitability',
                          title='WF: Investor Platform')

    def enter_info(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13):
        assert self.primInvObj is not None
        self.primInvObj.send_keys(q1)
        assert q1 in self.primInvObj.get_attribute("value")

        assert self.relInvExp is not None
        self.relInvExp.send_keys(q2)
        assert q2 in self.relInvExp.get_attribute("value")

        assert self.wilAccptRisk is not None
        self.wilAccptRisk.send_keys(q3)
        assert q3 in self.wilAccptRisk.get_attribute("value")

        assert self.maxInvHorizon is not None
        self.maxInvHorizon.send_keys(q4)
        assert q4 in self.maxInvHorizon.get_attribute("value")

        assert self.currentPortInvEq is not None
        self.currentPortInvEq.send_keys(q5)
        assert q5 in self.currentPortInvEq.get_attribute("value")

        assert self.currentPortInvBond is not None
        self.currentPortInvBond.send_keys(q6)
        assert q6 in self.currentPortInvBond.get_attribute("value")

        assert self.currentPortInvRE is not None
        self.currentPortInvRE.send_keys(q7)
        assert q7 in self.currentPortInvRE.get_attribute("value")

        assert self.currentPortInvOther is not None
        self.currentPortInvOther.send_keys(q8)
        assert q8 in self.currentPortInvOther.get_attribute("value")

        assert self.immedLiqWorth is not None
        self.immedLiqWorth.send_keys(q9)
        assert q9 in self.immedLiqWorth.get_attribute("value")

        assert self.annualLivExp is not None
        self.annualLivExp.send_keys(q10)
        assert q10 in self.annualLivExp.get_attribute("value")

        assert self.margPerTaxRt is not None
        self.margPerTaxRt.send_keys(q11)
        assert q11 in self.margPerTaxRt.get_attribute("value")

        assert self.iUnderstand is not None
        self.iUnderstand.send_keys(q12)
        assert q12 in self.iUnderstand.get_attribute("value")

        assert self.iHaveConduct is not None
        self.iHaveConduct.send_keys(q13)
        assert q13 in self.iHaveConduct.get_attribute("value")


    def invest(self, amount):
        assert self.invAmount is not None
        self.invAmount.send_keys(amount)
        #TODO: check the text below the field

        assert self.btnInvAmt is not None
        self.btnInvAmt.click()
        waitForAngular(self.driver)