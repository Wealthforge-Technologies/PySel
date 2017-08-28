from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class OEInvestmentPage(BasePage):
    offering = PageElement(xpath='//*[@id="offeringID"]/div/span[1]')
    subDate = PageElement(id_='investment.subscriptionDate')
    investType = PageElement(xpath='//*[@id="investorType"]/div/span[1]')
    payType = PageElement(xpath='//*[@id="paymentType"]/div/span[1]')
    invAmount = PageElement(id_='investment.payment.amount')
    invSubType = PageElement(xpath='//*[@id="investorSubType"]/div/span[1]')
    btnForward = PageElement(xpath='//*[@id="save"]/span/i')


    def __init__(self):
        BasePage.__init__(self,
                          url='https://ci-order-entry.wealthforge.org/investment',
                          title='Order Entry')

    def enter_info(self, offerq1, subDateq2, invTypeq3, payTypeq4, invAmtq5, invSubTyp):
        assert self.offering is not None
        self.offering.send_keys(offerq1)
        assert offerq1 in self.offering.get_attribute("value")

        assert self.subDate is not None
        self.subDate.send_keys(subDateq2)
        assert subDateq2 in self.subDate.get_attribute("value")

        assert self.investType is not None
        self.investType.send_keys(invTypeq3)
        assert invTypeq3 in self.investType.get_attribute("value")

        assert self.payType is not None
        self.payType.send_keys(payTypeq4)
        assert payTypeq4 in self.payType.get_attribute("value")

        assert self.invAmount is not None
        self.invAmount.send_keys(invAmtq5)
        assert invAmtq5 in self.invAmount.get_attribute("value")

        assert self.invSubType is not None
        self.invSubType.send_keys(invSubTyp)
        assert invSubTyp in self.invSubType.get_attribute("value")



    def clickForward(self):
        self.btnForward.click()
        waitForAngular(self.driver)