from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class IPLoginPage(BasePage):
    email = PageElement(id_='username')
    password = PageElement(id_='password')
    btnLogin = PageElement(id_='btnLogin')
    btnSignUp = PageElement(id_='btnSignUp')
    lnkForgotPassword = PageElement(id_='linkForgotPassword')
    print(type(btnLogin))

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/login/2eb2d7ff-1fa9-4f72-8dd5-e1527bf58cb3',  # TODO: separate the dpo uuid,
                          title='WF: Investor Platform')

    def login(self, username, password):
        self.email.send_keys(username)
        assert username in self.email.get_attribute("value")

        self.password.send_keys(password)
        assert password in self.password.get_attribute("value")


        self.btnLogin.click()
        waitForAngular(self.driver)

    def clickSignup(self):
        self.btnSignUp.click()
        waitForAngular(self.driver)
