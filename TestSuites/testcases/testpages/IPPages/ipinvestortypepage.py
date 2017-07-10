from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver
from selenium.webdriver.common.keys import Keys


class IPInvestorTypePage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/summary"""
    btnInvTypeIndiv = PageElement(id_='divInvestorTypeIndividual')
    btnInvTypeEntity = PageElement(id_='divInvestorTypeEntity')
    btnInvTypeMarried = PageElement(id_='divInvestorTypeMarried')
    btnInvTypeRepre = PageElement(id_='divInvestorTypeRepresentative')
    entityType = PageElement(id_='ddlEntityTypes')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/query',
                          title='WF: Investor Platform')


    def enter_info(self, entType):
        assert self.entityType is not None
        self.entityType.send_keys(entType)
        assert entType in self.entityType.get_attribute("value")


    def clickIndividual(self):
        self.divInvestorTypeIndividual.click()
        waitForAngular(self.driver)

    def clickEntity(self):
        self.divInvestorTypeEntity.click()
        waitForAngular(self.driver)

    def clickMarried(self):
        self.divInvestorTypeMarried.click()

    def clickRepresentative(self):
        self.divInvestorTypeRepresentative.click()



