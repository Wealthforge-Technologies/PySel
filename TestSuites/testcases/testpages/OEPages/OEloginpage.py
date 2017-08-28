from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class OELoginPage(BasePage):
    btnLogin = PageElement(xpath='//*[@id="dynamicFormContainer"]/md-card/md-card-actions/button/span')
    btnLogGoogle = PageElement(xpath='//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/button[1]/div[2]')


    def __init__(self):
        BasePage.__init__(self,
                          url='https://ci-order-entry.wealthforge.org/login',
                          title='Order Entry')

    def clickLogin(self):
        self.btnLogin.click()
        waitForAngular(self.driver)

    def clickGoogleLogin(self):
        self.btnLogGoogle.click()
        waitForAngular(self.driver)
