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
    newEntity = PageElement(id_='divNewInvestor')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/query',
                          title='WF: Investor Platform')


    def enter_info(self, entType):
        assert self.entityType is not None
        self.entityType.send_keys(entType)
        # assert entType in self.entityType.get_attribute("value")

    def clickNewEntity(self):
        self.newEntity.click()
        waitForAngular(self.driver)

    def clickIndividual(self):
        self.btnInvTypeIndiv.click()
        waitForAngular(self.driver)

    def clickEntity(self):
        self.btnInvTypeEntity.click()
        waitForAngular(self.driver)

    def clickMarried(self):
        self.btnInvTypeMarried.click()

    def clickRepresentative(self):
        self.btnInvTypeRepre.click()

    def clickReturnEntity(self):
        entityBox = self.driver.find_element_by_css_selector('[ng-if="type.code == query.investorType && showNew"]')
        entities = entityBox.find_elements_by_css_selector('[id^="divInv"]')
        entities[0].click()
        waitForAngular(self.driver)

    def clickReturnEntityByName(self, entName):
        '''
        clicks a returning entity given the name. Selects the first of multiple entries.
        :param entName: 
        '''
        entities = self.driver.find_elements_by_id("divInv" + entName.replace(" ", "_"))
        entities[0].click()
        waitForAngular(self.driver)

