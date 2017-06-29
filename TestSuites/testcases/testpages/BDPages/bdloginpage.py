from ..element import PageElement
# from ..element import ExtWebElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage

# click = ExtWebElement.clickw
# send_keys = ExtWebElement.send_keysw


class BDLoginPage(BasePage):
    email = PageElement(id_='username')
    password = PageElement(id_='password')
    btnLogin = PageElement(id_='btnLogin')

    def __init__(self):
        BasePage.__init__(self,
                          url='/login/#/',
                          title='WF: Login')

    #This method is a form submit for the BD login screen which leads to bdhomepage
    def login(self, username, password):
        self.email.send_keys(username)
        assert username in self.email.get_attribute("value")

        self.password.send_keys(password)
        assert password in self.password.get_attribute("value")

        self.btnLogin.click()
        waitForAngular(self.driver)
