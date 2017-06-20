from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class IPInvestorConfirmationPage(BasePage):
    chkBoxAffirmCC = PageElement(id_='chkAffirmCreditCheck')
    chkBoxAffirmTC = PageElement(id_='chkAffirmTermsAndConditions')


    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/confirmation',
                          title='WF: Investor Platform')


