from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .element import PageElement
from .testpageutilities.waitforangular import waitForAngular
from .basepage import BasePage

class IPIndividualInvestorRegistrationPage(BasePage):
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

    def enter_info(self, first, last, dob, ssn, address, addr2, city, state, zip, phone, email):
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

        assert self.address is not None
        self.address.send_keys(address)
        assert address in self.address.get_attribute("value")

        assert self.addressTwo is not None
        self.addressTwo.send_keys(addr2)
        assert addr2 in self.addressTwo.get_attribute("value")

        assert self.city is not None
        self.city.send_keys(city)
        assert city in self.city.get_attribute("value")

        assert self.state is not None
        Select(self.state).select_by_visible_test(state)
        #self.state.send_keys(state)
        assert state in self.state.get_attribute("value")

        assert self.zipCode is not None
        self.zipCode.send_keys(zip)
        assert zip in self.zipCode.get_attribute("value")

        assert self.phoneNumber is not None
        self.phoneNumber.send_keys(phone)
        assert phone in self.phoneNumber.get_attribute("value")

        assert self.email is not None
        self.email.send_keys(email)
        assert email in self.email.get_attribute("value")


        def clickContinue(self):
            self.btnContinue.click()
            waitForAngular(self.driver)
