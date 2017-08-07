from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class IPCreateNewPasswordPage(BasePage):
    password = PageElement(id_='username')
    confPassword = PageElement(id_='password2')
    btnSave = PageElement(css='[ng-click="resetPass()"]')

    def __init__(self, confirmUrl):
        BasePage.__init__(self,
                          url=confirmUrl,
                          title='WF: Investor Platform')

    def enter_info(self, pswrd, confPwd):
        assert self.password is not None
        self.password.send_keys(pswrd)
        assert pswrd in self.password.get_attribute("value")

        assert self.confPassword is not None
        self.confPassword.send_keys(confPwd)
        assert confPwd in self.confPassword.get_attribute("value")


    def clickSave(self):
        self.btnSave.click()
        waitForAngular(self.driver)

        while True:
            pass



