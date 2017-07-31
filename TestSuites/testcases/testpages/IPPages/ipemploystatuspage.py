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
    marrEmployStat = PageElement(xpath='//*[@id="stepform"]/div/employment/div[2]/div[2]/div[1]/div/select')
    rbMarrEngagedYes = PageElement(xpath='//*[@id="stepform"]/div/employment/div[2]/div[2]/div[2]/input[1]')
    rbMarrEngagedNo = PageElement(xpath='//*[@id="stepform"]/div/employment/div[2]/div[2]/div[2]/input[2]')
    rbMarrFINRAYes = PageElement(xpath='//*[@id="stepform"]/div/employment/div[2]/div[2]/div[3]/input[1]')
    rbMarrFINRANo = PageElement(xpath='//*[@id="stepform"]/div/employment/div[2]/div[2]/div[3]/input[2]')
    cRDNumber = PageElement(xpath='//*[@id="stepform"]/div/employment/div[2]/div[2]/div[4]/input')
    rbSpMarrFINRAYes = PageElement(xpath='//*[@id="stepform"]/div/employment/div[2]/div[2]/div[5]/input[1]')
    rbSpMarrFINRANo = PageElement(xpath='//*[@id="stepform"]/div/employment/div[2]/div[2]/div[5]/input[2]')
    spCRDNumber = PageElement(xpath='//*[@id="stepform"]/div/employment/div[2]/div[2]/div[6]/input')


    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/employment',
                          title='WF: Investor Platform')

    #Enter Employment Info for Individual
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

    #Enter Employment Info for Married
    def enter_married_info(self, marrEmpStat, firstRadioButton, secondRadioButton, crdNum, thirdRadioButton, spCrdNum):
            # radiobuttons and CRD are optional because they are only if you select Currently Employed or Self Employed

        assert self.marrEmployStat is not None
        Select(self.marrEmployStat).select_by_visible_text(marrEmpStat)

        # Which to select for the first radio button group?
        if firstRadioButton:
            assert self.rbMarrEngagedYes is not None
            self.rbMarrEngagedYes.click()
        else:
            assert self.rbMarrEngagedNo is not None
            self.rbMarrEngagedNo.click()

        # Which to select for the second radio button group and if yes then also enter a CRD
        if secondRadioButton:
            assert self.rbMarrFINRAYes is not None
            self.rbMarrFINRAYes.click()

        else:
            assert self.rbMarrFINRANo is not None
            self.rbMarrFINRANo.click()

        assert self.cRDNumber is not None
        self.cRDNumber.send_keys(crdNum)
        assert crdNum in self.cRDNumber.get_attribute("value")

        # To select Spouses FINRA registration
        if thirdRadioButton:
            assert self.rbSpMarrFINRAYes is not None
            self.rbSpMarrFINRAYes.click()

        else:
            assert self.rbSpMarrFINRANo is not None
            self.rbSpMarrFINRANo.click()

        assert self.spCRDNumber is not None
        self.spCRDNumber.send_keys(spCrdNum)
        assert spCrdNum in self.spCRDNumber.get_attribute("value")

    #Verify Employment Information

    def verify_info(self, empStat, firstRadioButton=False, secondRadioButton=False, crd=''):
        # radiobuttons and CRD are optional because they are only if you select Currently Employed or Self Employed

        assert self.employStatus is not None

        # Which to select for the first radio button group?
        if firstRadioButton:
            assert self.otherOpportYes is not None
        else:
            assert self.otherOpportNo is not None


        # Which to select for the second radio button group and if yes then also enter a CRD
        if secondRadioButton:
            assert self.otherOpportYes is not None

            assert self.otherOpportYes is not None

        else:
            assert self.otherOpportNo is not None

    #Verify Married Employment Info
    def verify_married_info(self, marrEmpStat, firstRadioButton, secondRadioButton, crdNum, thirdRadioButton, spCrdNum):
            # radiobuttons and CRD are optional because they are only if you select Currently Employed or Self Employed

        assert self.marrEmployStat is not None

        # Which to select for the first radio button group?
        if firstRadioButton:
            assert self.rbMarrEngagedYes is not None
        else:
            assert self.rbMarrEngagedNo is not None

        # Which to select for the second radio button group and if yes then also enter a CRD
        if secondRadioButton:
            assert self.rbMarrFINRAYes is not None

        else:
            assert self.rbMarrFINRANo is not None

        assert self.cRDNumber is not None
        assert crdNum in self.cRDNumber.get_attribute("value")

        # To select Spouses FINRA registration
        if thirdRadioButton:
            assert self.rbSpMarrFINRAYes is not None

        else:
            assert self.rbSpMarrFINRANo is not None

        assert self.spCRDNumber is not None
        assert spCrdNum in self.spCRDNumber.get_attribute("value")


