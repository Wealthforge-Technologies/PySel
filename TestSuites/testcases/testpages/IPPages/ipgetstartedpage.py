from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver

class IPGetStarted(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/ready/"""
    # btnStart = PageElement(id_='btnStart')
    btnStart = PageElement(xpath='//*[@id="resumeProgress"]/div[2]/button')
    #TODO: Resume investments

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/ready',
                          title='WF: Investor Platform')

    # def __init__(self):
    #     self.driver = getOrCreateWebdriver()
    #     self.expected_landing_url = "https://qa1.wealthforge.org/IP/#/ready/"
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
    #             lambda wait: self.driver.current_url in self.expected_landing_url)
    #     finally:
    #         assert self.expected_landing_url in self.driver.current_url
    #     waitForAngular(self.driver)

    def land(self):
        self.driver.get(self.expected_landing_url)

    #This method is a form submit for the IP Get Started page
    # def clickGetStarted(self):
    #
    #     self.btnStart.click()
    #     waitForAngular(self.driver)
