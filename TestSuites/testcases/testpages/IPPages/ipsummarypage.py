from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver

class IPSummaryPage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/summary"""
    btnBack = PageElement(id_='btnBack')
    btnContinue = PageElement(id_='btnContinue')
    btnInvestAmount = PageElement(id_='investAmount')
    btnQuickContinue = PageElement(id_='btnQuickContinue')
    header = PageElement(id_='hHeadLine')
    offerTab = PageElement(name='offerTab')
    filesTab = PageElement(name='filesTab')
    invAmount = PageElement(id_='invAmnt')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/summary',
                          title='WF: Investor Platform')

    # def __init__(self):
    #     self.driver = getOrCreateWebdriver()
    #     self.expected_landing_url = "https://qa1.wealthforge.org/IP/#/summary"
    #     self.expected_title = "WF: Investor Platform"
    #
    # def is_expected_title(self):
    #     """Verifies that the hardcoded text "WF: Investor Platform" appears in page title"""
    #     try:
    #         wait = WebDriverWait(self.driver, 5).until(
    #             EC.title_contains(self.expected_title))
    #     finally:
    #         assert self.expected_title in self.driver.title
    #     waitForAngular(self.driver)
    #
    #
    # def is_expected_landing_url(self):
    #     """Verifies that the hardcoded text "WF: Investor Platform" appears in page title"""
    #     try:
    #         wait = WebDriverWait(self.driver, 5).until(
    #             lambda wait: self.driver.current_url == self.expected_landing_url)
    #     finally:
    #         assert self.expected_landing_url in self.driver.current_url
    #     waitForAngular(self.driver)
    #
    # def land(self):
    #     self.driver.get(self.expected_landing_url)

    #This method is a form submit for the IP Summary Page
    def clickContinue(self):

        self.btnContinue.click()
        waitForAngular(self.driver)
