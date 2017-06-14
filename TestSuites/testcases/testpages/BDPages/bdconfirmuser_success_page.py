from selenium.webdriver.support.ui import WebDriverWait
from ..element import PageElement
from ..basepage import BasePage
from ..testpageutilities.waitforangular import waitForAngular
from ..testpageutilities import getOrCreateWebdriver


class BDConfirmUserSuccessPage(BasePage):
    submit_button = PageElement(id_='btnReturnToLogin')

    def __init__(self):
        BasePage.__init__(self,
                          url='',
                          title='WF: Login')

    # def __init__(self):
    #     self.driver = getOrCreateWebdriver()
    #     self.expected_title = "WF: Login"
    #
    # def is_expected_title(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 5).until(
    #             EC.title_contains(self.expected_title))
    #     finally:
    #         assert self.expected_title in self.driver.title
    #     waitForAngular(self.driver)

    def submit(self):
        assert self.submit_button is not None
        self.submit_button.click()
        waitForAngular(self.driver)
