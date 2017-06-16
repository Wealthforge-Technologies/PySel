from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from selenium.webdriver.support.ui import Select


class IPEmploymentStatusPage(BasePage):
    employStatus = PageElement(id_='ddlInvestorEmploymentStatus')
    otherOpportYes = PageElement(id_='rbOtherOpportunitiesYes')
    otherOpportNo = PageElement(id_='rbOtherOpportunitiesNo')
    rbFINRAYes = PageElement(id_='rbFINRAYes')
    rbFINRANo = PageElement(id_='rbFINRANo')
    txtCRDNumber = PageElement(id_='txtCRDNumber')

    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/employment',
                          title='WF: Investor Platform')

    def enter_info(self, empStat, firstRadioButton=False, secondRadioButton=False, crd=''):
        # radiobuttons and CRD are optional because they are only if you select Currently Employed or Self Employed

        assert self.employStatus is not None
        Select(self.employStatus).select_by_visible_text(empStat)

        # Which to select for the first radio button group?
        if firstRadioButton:
            assert self.otherOpportYes is not None
            self.otherOpportYes.click()
        else:
            assert self.otherOpportNo is not None
            self.otherOpportNo.click()


        # Which to select for the second radio button group and if yes then also enter a CRD
        if secondRadioButton:
            assert self.otherOpportYes is not None
            self.rbFINRAYes.click()

            assert self.otherOpportYes is not None
            self.txtCRDNumber.send_keys(crd)

        else:
            assert self.otherOpportNo is not None
            self.rbFINRANo.click()

