from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class IPInvestorAccredidationPage(BasePage):
    btnNetWorth = PageElement(id_='divTypeNet_Worth')
    btnIncome = PageElement(id_='divTypeIncome')
    btnNotAccred = PageElement(id_='divTypeNotAccredited')
    btnIncOrNet = PageElement(id_='divTypeIncome_or_Net_Worth')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/accreditation',
                          title='WF: Investor Platform')

    def enter_info(self, net, income, notAcc, incOrNet):
        assert self.btnNetWorth is not None
        self.btnNetWorth.send_keys(net)
        assert net in self.btnNetWorth.get_attribute("value")

        assert self.btnIncome is not None
        self.btnIncome.send_keys(income)
        assert income in self.btnIncome.get_attribute("value")

        assert self.btnNotAccred is not None
        self.btnNotAccred.send_keys(notAcc)
        assert notAcc in self.btnNotAccred.get_attribute("value")

        assert self.btnIncOrNet is not None
        self.btnIncOrNet.send_keys(incOrNet)
        assert incOrNet in self.btnIncOrNet.get_attribute("value")


    def land(self):
        self.driver.get(self.expected_landing_url)


        def clickContinue(self):
            self.btnContinue.click()
            waitForAngular(self.driver)

        def clickNetWorth(self):
            self.divTypeNet_Worth.click()
            waitForAngular(self.driver)

        def clickIncOrNW(self):
            self.divTypeIncome_or_Net_Worth.click()
            waitForAngular(self.driver)

