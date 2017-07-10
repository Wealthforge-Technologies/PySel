from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from selenium.webdriver.support.ui import Select

class IPMarriedInvestorRegistrationPage(BasePage):
    btnBack = PageElement(id_='Back')
    btnContinue = PageElement(id_='btnContinue')
    firstName = PageElement(id_='txtInvestorFirstName')
    lastName = PageElement(id_='txtInvestorLastName')
    dateOfBirth = PageElement(id_='txtInvestorDOB')
    socialSec = PageElement(id_='txtInvestorSSN')
    address1 = PageElement(id_='txtInvestorAddress1')
    address2 = PageElement(id_='txtInvestorAddress2')
    city = PageElement(id_='txtInvestorCity')
    state = PageElement(xpath='//*[@id="ddlInvestorStateProvs"]/select')
    zipCode = PageElement(id_='txtInvestorPostalCode')
    phoneNumber = PageElement(id_='txtInvestorPhone')
    email = PageElement(id_='txtInvestorEmail')
    spouseFN = PageElement(id_="txtSpouseFirstName")
    spouseLN = PageElement(id_="txtSpouseLastName")
    spouseDOB = PageElement(id_="txtSpouseDOB")
    spouseSSN = PageElement(id_="txtSpouseSSN")
    spousePhone = PageElement(id_="txtSpousePhone")
    spouseEmail = PageElement(id_="txtSpouseEmail")
    spouseEmailConf = PageElement(id_="txtSpouseEmailConfirm")

    def enter_info(self, first, last, dob, ssn, address, addr2, city, state, zip, phone, email, spouseFN, spouseLN, spouseDOB, spouseSSN, spousePhone, spouseEmail, spouseEmailConf):
        assert self.firstName is not None
        self.firstName.send_keys(first)
        assert first in self.firstName.get_attribute("value")

        assert self.lastName is not None
        self.lastName.send_keys(last)
        assert last in self.lastName.get_attribute("value")

        assert self.dateOfBirth is not None
        self.dateOfBirth.send_keys(dob)
        assert dob in self.dateOfBirth.get_attribute("value")

        assert self.socialSec is not None
        self.socialSec.send_keys(ssn)
        assert ssn in self.socialSec.get_attribute("value")

        assert self.address1 is not None
        self.address1.send_keys(address)
        assert address in self.address1.get_attribute("value")

        assert self.address2 is not None
        self.address2.send_keys(addr2)
        assert addr2 in self.address2.get_attribute("value")

        assert self.city is not None
        self.city.send_keys(city)
        assert city in self.city.get_attribute("value")

        assert self.state is not None
        Select(self.state).select_by_visible_text(state)
        #self.state.send_keys(state)
        assert state in self.state.get_attribute("value").all_selected_options[0].get_attribute("textContent")

        assert self.zipCode is not None
        self.zipCode.send_keys(zip)
        assert zip in self.zipCode.get_attribute("value")

        assert self.phoneNumber is not None
        self.phoneNumber.send_keys(phone)
        assert phone in self.phoneNumber.get_attribute("value")

        assert self.email is not None
        self.email.send_keys(email)
        assert email in self.email.get_attribute("value")

        assert self.spouseFN is not None
        self.spouseFN.send_keys(spouseFN)
        assert spouseFN in self.spouseFN.get_attribute("value")

        assert self.spouseLN is not None
        self.spouseLN.send_keys(spouseLN)
        assert spouseLN in self.spouseLN.get_attribute("value")

        assert self.spouseDOB is not None
        self.spouseDOB.send_keys(spouseDOB)
        assert spouseDOB in self.spouseDOB.get_attribute("value")

        assert self.spouseSSN is not None
        self.spouseSSN.send_keys(spouseSSN)
        assert spouseSSN in self.spouseSSN.get_attribute("value")

        assert self.spousePhone is not None
        self.spousePhone.send_keys(spousePhone)
        assert spousePhone in self.spousePhone.get_attribute("value")

        assert self.spouseEmail is not None
        self.spouseEmail.send_keys(spouseEmail)
        assert spouseEmail in self.spouseEmail.get_attribute("value")

        assert self.spouseEmailConf is not None
        self.spouseEmailConf.send_keys(spouseEmailConf)
        assert spouseEmailConf in self.spouseEmailConf.get_attribute("value")


        def clickContinue(self):
            self.btnContinue.click()
            waitForAngular(self.driver)
