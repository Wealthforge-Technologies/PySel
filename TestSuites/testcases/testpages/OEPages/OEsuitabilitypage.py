from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class OESuitabilityPage(BasePage):
    chkBoxAnswerQs = PageElement(xpath='//*[@id="divhasSuitability"]/div/md-input-container/div/div[1]/div/md-checkbox/label/div')
    primInvObj = PageElement(xpath='//*[@id="std_a_objective"]/div/span[1]')
    invExperience = PageElement(xpath='//*[@id="std_b_experience"]/div/span[1]')
    risk = PageElement(xpath='//*[@id="std_c_risk"]/div/span[1]')
    horizon = PageElement(xpath='//*[@id="std_d_horizon"]/div/span[1]')
    allocEquities = PageElement(xpath='//*[@id="std_e_allocationEquities"]/div/span[1]')
    allocBonds = PageElement(xpath='//*[@id="std_f_allocationBonds"]/div/span[1]')
    allocRealEstate = PageElement(xpath='//*[@id="std_g_allocationRealEstate"]/div')
    allocOther = PageElement(xpath='//*[@id="std_h_allocationOtherInvestments"]/div/span[1]')
    liquidity = PageElement(xpath='//*[@id="std_i_liquidity"]/div/span[1]')
    annualExpenses = PageElement(xpath='//*[@id="std_j_annualExpenses"]/div/span[1]')
    marginalTaxRt = PageElement(xpath='//*[@id="std_k_marginalTaxRate"]/div/span[1]')
    acceptRisk = PageElement(xpath='//*[@id="std_l_acceptRisk"]/div/span[1]')
    dueDiligence = PageElement(xpath='//*[@id="std_m_dueDiligence"]/div/span[1]')
    btnForward = PageElement(xpath='//*[@id="save"]/span/i')


    def __init__(self):
        BasePage.__init__(self,
                          url='https://ci-order-entry.wealthforge.org/suitability',
                          title='Order Entry')

    def enter_info(self, primInv, invExp, risk, horiz, allocEq, allocBond, allocRE, allocOther, liquid, annExp, margTxRt, accRisk, dueDill):
        assert self.primInvObj is not None
        self.primInvObj.send_keys(primInv)
        assert primInv in self.primInvObj.get_attribute("value")

        assert self.invExperience is not None
        self.invExperience.send_keys(invExp)
        assert invExp in self.invExperience.get_attribute("value")

        assert self.risk is not None
        self.risk.send_keys(risk)
        assert risk in self.risk.get_attribute("value")

        assert self.horizon is not None
        self.horizon.send_keys(horiz)
        assert horiz in self.horizon.get_attribute("value")

        assert self.allocEquities is not None
        self.allocEquities.send_keys(allocEq)
        assert allocEq in self.allocEquities.get_attribute("value")

        assert self.allocBonds is not None
        self.allocBonds.send_keys(allocBond)
        assert allocBond in self.allocBonds.get_attribute("value")

        assert self.allocRealEstate is not None
        self.allocRealEstate.send_keys(allocRE)
        assert allocRE in self.allocRealEstate.get_attribute("value")

        assert self.allocOther is not None
        self.allocOther.send_keys(allocOther)
        assert allocOther in self.allocOther.get_attribute("value")

        assert self.liquidity is not None
        self.liquidity.send_keys(liquid)
        assert liquid in self.liquidity.get_attribute("value")

        assert self.annualExpenses is not None
        self.annualExpenses.send_keys(annExp)
        assert annExp in self.annualExpenses.get_attribute("value")

        assert self.marginalTaxRt is not None
        self.marginalTaxRt.send_keys(margTxRt)
        assert margTxRt in self.marginalTaxRt.get_attribute("value")

        assert self.acceptRisk is not None
        self.acceptRisk.send_keys(accRisk)
        assert accRisk in self.acceptRisk.get_attribute("value")

        assert self.dueDiligence is not None
        self.dueDiligence.send_keys(dueDill)
        assert dueDill in self.dueDiligence.get_attribute("value")

    def clickAnswerSuitabilityQs(self):
        self.chkBoxAnswerQs.click()
        waitForAngular(self.driver)

    def clickForward(self):
        self.btnForward.click()
        waitForAngular(self.driver)