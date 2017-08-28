from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage


class OEInvestorPage(BasePage):
    accreditType = PageElement(xpath='//*[@id="accreditationType"]/div/span[1]')
    firstName = PageElement(id_='investor.individual.firstName')
    lastName = PageElement(id_='investor.individual.lastName')
    dateOfBirth = PageElement(id_='vault.individual.dateOfBirth')
    socialSN = PageElement(id_='vault.individual.ssn')
    phoneNumber = PageElement(id_='investor.individual.primaryPhone')
    email = PageElement(id_='investor.individual.emailAddress')
    streetAddress = PageElement(id_='investor.individual.address.street1')
    apartNum = PageElement(id_='investor.individual.address.street2"')
    city = PageElement(id_='investor.individual.address.city')
    stateProvence = PageElement(xpath='//*[@id="stateProv"]/div/span[1]')
    zipCode = PageElement(id_='investor.individual.address.postalCode')
    chkBoxFinraInv = PageElement(xpath='//*[@id="divisFINRA"]/div/md-input-container/div/div[1]/div/md-checkbox/label/div')
    spouseFN = PageElement(id_='investor.spouse.firstName')
    spouseLN = PageElement(id_='investor.spouse.lastName')
    spouseDOB = PageElement(id_='vault.spouse.dateOfBirth')
    spouseSSN = PageElement(id_='vault.spouse.ssn')
    spousePhoneNum = PageElement(id_='investor.spouse.primaryPhone')
    spouseEmail = PageElement(id_='investor.spouse.emailAddress')
    btnForward = PageElement(xpath='//*[@id="save"]/span/i')


    def __init__(self):
        BasePage.__init__(self,
                          url='https://ci-order-entry.wealthforge.org/investor',
                          title='Order Entry')

    def enter_info(self, accType, fName, lName, dob, socialSN, phNum, email, stAddress, city, state, zip):
        assert self.accreditType is not None
        self.accreditType.send_keys(accType)
        assert accType in self.accreditType.get_attribute("value")

        assert self.firstName is not None
        self.firstName.send_keys(fName)
        assert fName in self.firstName.get_attribute("value")

        assert self.lastName is not None
        self.lastName.send_keys(lName)
        assert lName in self.lastName.get_attribute("value")

        assert self.dateOfBirth is not None
        self.dateOfBirth.send_keys(dob)
        assert dob in self.dateOfBirth.get_attribute("value")

        assert self.socialSN is not None
        self.socialSN.send_keys(socialSN)
        assert socialSN in self.socialSN.get_attribute("value")

        assert self.phoneNumber is not None
        self.phoneNumber.send_keys(phNum)
        assert phNum in self.phoneNumber.get_attribute("value")

        assert self.email is not None
        self.email.send_keys(email)
        assert email in self.email.get_attribute("value")

        assert self.streetAddress is not None
        self.streetAddress.send_keys(stAddress)
        assert stAddress in self.streetAddress.get_attribute("value")

        assert self.city is not None
        self.city.send_keys(city)
        assert city in self.city.get_attribute("value")

        assert self.stateProvence is not None
        self.stateProvence.send_keys(state)
        assert state in self.stateProvence.get_attribute("value")

        assert self.zipCode is not None
        self.zipCode.send_keys(zip)
        assert zip in self.zipCode.get_attribute("value")

    def clickForward(self):
        self.btnForward.click()
        waitForAngular(self.driver)