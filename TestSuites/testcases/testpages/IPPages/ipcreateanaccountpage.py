from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

class IPCreateAnAccountPage(BasePage):
    firstName = PageElement(id_='fname')
    lastName = PageElement(id_='lname')
    email = PageElement(id_='email')
    confirmEmail = PageElement(id_='confemail')
    chkBoxAffilFA = PageElement(id_='chkAffiliatedWithFinancialAdvisor')
    btnSignUp = PageElement(id_='btnSignUp')
    btnCreateAcct = PageElement(xpath='//*[@id="signupForm"]/div/div[6]/input')
    btnReturnToLogin = PageElement(xpath='/html/body/div[2]/div/ui-view/email/div[2]/div/input')


    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/signup/',
                          title='WF: Investor Platform')

    def enter_info(self, first, last, email, confEmail):


        print(email)


        assert self.firstName is not None
        self.firstName.send_keys(first)
        assert first in self.firstName.get_attribute("value")

        assert self.lastName is not None
        self.lastName.send_keys(last)
        assert last in self.lastName.get_attribute("value")

        assert self.email is not None
        self.email.send_keys(email)
        assert email in self.email.get_attribute("value")

        assert self.confirmEmail is not None
        self.confirmEmail.send_keys(confEmail)
        assert confEmail in self.confirmEmail.get_attribute("value")

    def clickSignUp(self):
        self.btnSignUp.click()
        waitForAngular(self.driver)

    def clickCreateAccount(self):
        self.btnCreateAcct.click()
        waitForAngular(self.driver)

    def clickReturnToLogin(self):
        self.btnReturnToLogin.click()
        waitForAngular(self.driver)


