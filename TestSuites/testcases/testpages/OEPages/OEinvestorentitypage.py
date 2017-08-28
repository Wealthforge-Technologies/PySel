from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class OEInvestorPage(BasePage):
    accreditType = PageElement(xpath='//*[@id="accreditationType"]/div')
    entityName = PageElement(id_='investor.entity.name')
    signatoryName = PageElement(id_='investor.entity.signatoryName')
    signatoryTitle = PageElement(id_='investor.entity.signatoryTitle')
    empIDNum = PageElement(id_='vault.entity.ein')
    socialSecNum = PageElement(id_='vault.entity.ssn')
    centIndexKey = PageElement(id_='investor.entity.cik')
    businessAddress = PageElement(id_='investor.entity.address.street1')
    aptSuite = PageElement(id_='investor.entity.address.street2')
    city = PageElement(id_='investor.entity.address.city')
    stateProvence = PageElement(xpath='//*[@id="stateProv"]/div')
    zipCode = PageElement(id_='investor.entity.address.postalCode')
    phoneNumber = PageElement(id_='investor.entity.primaryPhone')
    email = PageElement(id_='investor.entity.emailAddress')
    btnForward = PageElement(xpath='//*[@id="save"]/span/i')


    def __init__(self):
        BasePage.__init__(self,
                          url='https://ci-order-entry.wealthforge.org/investor',
                          title='Order Entry')

    def enter_info(self, accType, entName, sigName, sigTitle, empID, ssn, cik, busiAdd, aptSui, city, state, zip, phone, email):
        assert self.accreditType is not None
        self.accreditType.send_keys(accType)
        assert accType in self.accreditType.get_attribute("value")

        assert self.entityName is not None
        self.entityName.send_keys(entName)
        assert entName in self.entityName.get_attribute("value")

        assert self.signatoryName is not None
        self.signatoryName.send_keys(sigName)
        assert sigName in self.signatoryName.get_attribute("value")

        assert self.signatoryTitle is not None
        self.signatoryTitle.send_keys(sigTitle)
        assert sigTitle in self.signatoryTitle.get_attribute("value")

        assert self.empIDNum is not None
        self.empIDNum.send_keys(empID)
        assert empID in self.empIDNum.get_attribute("value")

        assert self.socialSecNum is not None
        self.socialSecNum.send_keys(ssn)
        assert ssn in self.socialSecNum.get_attribute("value")

        assert self.centIndexKey is not None
        self.centIndexKey.send_keys(cik)
        assert cik in self.centIndexKey.get_attribute("value")

        assert self.businessAddress is not None
        self.businessAddress.send_keys(busiAdd)
        assert busiAdd in self.businessAddress.get_attribute("value")

        assert self.aptSuite is not None
        self.aptSuite.send_keys(aptSui)
        assert aptSui in self.aptSuite.get_attribute("value")

        assert self.city is not None
        self.city.send_keys(city)
        assert city in self.city.get_attribute("value")

        assert self.stateProvence is not None
        self.stateProvence.send_keys(state)
        assert state in self.stateProvence.get_attribute("value")

        assert self.zipCode is not None
        self.zipCode.send_keys(zip)
        assert zip in self.zipCode.get_attribute("value")

        assert self.phoneNumber is not None
        self.phoneNumber.send_keys(phone)
        assert phone in self.phoneNumber.get_attribute("value")

        assert self.email is not None
        self.email.send_keys(email)
        assert email in self.email.get_attribute("value")

    def clickForward(self):
        self.btnForward.click()
        waitForAngular(self.driver)