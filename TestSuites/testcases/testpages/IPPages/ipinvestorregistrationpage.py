from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver
import testutilities.Settings
from selenium.webdriver.support.ui import Select


class IPInvestorTypePage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/ind/registration"""
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


    def __init__(self):
        BasePage.__init__(self,
                          url='/IP/#/ind/registration',
                          title='WF: Investor Platform')



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
        # print(self.socialSec.get_attribute("value"))
        # print(ssn)
        # if(self.socialSec.get_attribute("value") == ssn):
        #     print('equ')



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
        # self.state.send_keys(state)
        assert state in Select(self.state).all_selected_options[0].get_attribute("textContent")

        assert self.zipCode is not None
        self.zipCode.send_keys(zip)
        assert zip in self.zipCode.get_attribute("value")

        assert self.phoneNumber is not None
        self.phoneNumber.send_keys(phone)
        assert phone in self.phoneNumber.get_attribute("value")

        assert self.email is not None
        self.email.send_keys(email)
        assert email in self.email.get_attribute("value")

    #Verify Registration for Returning Individual Investor
    def verify_info(self, first, last, dob, ssn, address, addr2, city, state, zip, phone, email):
        assert self.firstName is not None
        assert first in self.firstName.get_attribute("value")

        assert self.lastName is not None
        assert last in self.lastName.get_attribute("value")

        assert self.dateOfBirth is not None
        assert dob in self.dateOfBirth.get_attribute("value")

        assert self.socialSec is not None
        assert ssn in self.socialSec.get_attribute("value")

        assert self.address1 is not None
        assert address in self.address1.get_attribute("value")

        assert self.address2 is not None
        assert addr2 in self.address2.get_attribute("value")

        assert self.city is not None
        assert city in self.city.get_attribute("value")

        assert self.state is not None
        # self.state.send_keys(state)
        assert state in Select(self.state).all_selected_options[0].get_attribute("textContent")

        assert self.zipCode is not None
        assert zip in self.zipCode.get_attribute("value")

        assert self.phoneNumber is not None
        assert phone in self.phoneNumber.get_attribute("value")

        assert self.email is not None
        assert email in self.email.get_attribute("value")

    def clickContinue(self):
        self.btnContinue.click()
        waitForAngular(self.driver)
