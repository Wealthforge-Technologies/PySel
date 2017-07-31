from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from selenium.webdriver.support.ui import Select

class IPEntityInvestorRegistrationPage(BasePage):
    btnBack = PageElement(id_='Back')
    btnContinue = PageElement(id_='btnContinue')
    entityName = PageElement(id_='txtInvestorName')
    signatoryName = PageElement(id_='txtInvestorSignatoryName')
    signatoryTitle = PageElement(id_='txtInvestorSignatoryTitle')
    investorEIN = PageElement(id_='txtInvestorEIN')
    socialSec = PageElement(id_='txtInvestorSSN')
    address1 = PageElement(id_='txtInvestorAddress1')
    address2 = PageElement(id_='txtInvestorAddress2')
    city = PageElement(id_='txtInvestorCity')
    state = PageElement(xpath='//*[@id="ddlInvestorStateProvs"]/select')
    zipCode = PageElement(id_='txtInvestorPostalCode')
    phoneNumber = PageElement(id_='txtInvestorPhone')
    email = PageElement(id_='txtInvestorEmail')

    #Enter info for entities
    # TODO: Manage other entity types
    def enter_info(self, entName, sigName, sigTitle, ein,  ssn, address, addr2, city, state, zip, phone, email):
        assert self.entityName is not None
        self.entityName.send_keys(entName)
        assert entName in self.entityName.get_attribute("value")

        assert self.signatoryName is not None
        self.signatoryName.send_keys(sigName)
        assert sigName in self.signatoryName.get_attribute("value")

        assert self.signatoryTitle is not None
        self.signatoryTitle.send_keys(sigTitle)
        assert sigTitle in self.signatoryTitle.get_attribute("value")

        assert self.investorEIN is not None
        self.investorEIN.send_keys(ein)
        assert ein in self.investorEIN.get_attribute("value")

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
        #assert state in self.state.get_attribute("value").all_selected_options[0].get_attribute("textContent")

        assert self.zipCode is not None
        self.zipCode.send_keys(zip)
        assert zip in self.zipCode.get_attribute("value")

        assert self.phoneNumber is not None
        self.phoneNumber.send_keys(phone)
        assert phone in self.phoneNumber.get_attribute("value")

        assert self.email is not None
        self.email.send_keys(email)
        assert email in self.email.get_attribute("value")

    #Returning User - Verify Info Entered
    #TODO: Manage other entity types
    def verify_info(self, entName, sigName, sigTitle, ein, ssn, address, addr2, city, state, zip, phone, email):
        assert self.entityName is not None
        assert entName in self.entityName.get_attribute("value")

        assert self.signatoryName is not None
        assert sigName in self.signatoryName.get_attribute("value")

        assert self.signatoryTitle is not None
        assert sigTitle in self.signatoryTitle.get_attribute("value")

        assert self.investorEIN is not None
        assert ein in self.investorEIN.get_attribute("value")

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
        # assert state in self.state.get_attribute("value").all_selected_options[0].get_attribute("textContent")

        assert self.zipCode is not None
        assert zip in self.zipCode.get_attribute("value")

        assert self.phoneNumber is not None
        assert phone in self.phoneNumber.get_attribute("value")

        assert self.email is not None
        assert email in self.email.get_attribute("value")

    def clickContinue(self):
        self.btnContinue.click()
        waitForAngular(self.driver)
