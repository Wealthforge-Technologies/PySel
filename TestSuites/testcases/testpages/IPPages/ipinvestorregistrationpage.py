from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver

class IPInvestorTypePage(BasePage):
    """QA Get Started page. I.e. https://qa1.wealthforge.org/IP/#/ind/registration"""
    btnBack = PageElement(id_='Back')
    btnContinue = PageElement(id_='btnContinue')
    firstName = PageElement(id_='txtInvestorFirstName')
    lastName = PageElement(id_='txtInvestorLastName')
    dateOfBirth = PageElement(id_='txtInvestorDOB')
    socialSec = PageElement(id_='txtInvestorSSN')
    address1 = PageElement(id_='txtInvestorAddress1')
    address2 = PageElement(id_='txtInvestorAddress2')
    city = PageElement(id_='txtInvestorCity')
    state = PageElement(id_='ddlInvestorStateProvs')
    zipCode = PageElement(id_='txtInvestorPostalCode')
    phoneNumber = PageElement(id_='txtInvestorPhone')
    email = PageElement(id_='txtInvestorEmail')

    def __init__(self):
        self.driver = getOrCreateWebdriver()
        self.expected_landing_url = "https://qa1.wealthforge.org/IP/#/ind/registration"
        self.expected_title = "WF: Investor Platform"

    def is_expected_title(self):
        """Verifies that the hardcoded text "WF: Investor Platform" appears in page title"""
        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(self.expected_title))
        finally:
            assert self.expected_title in self.driver.title
        waitForAngular(self.driver)


    def is_expected_landing_url(self):
        """Verifies that the hardcoded text "WF: Investor Platform" appears in page title"""
        try:
            wait = WebDriverWait(self.driver, 5).until(
                lambda wait: self.driver.current_url == self.expected_landing_url)
        finally:
            assert self.expected_landing_url in self.driver.current_url
        waitForAngular(self.driver)

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
        self.state.send_keys(state)
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

    def land(self):
        self.driver.get(self.expected_landing_url)


        def clickContinue(self):
            self.btnContinue.click()
            waitForAngular(self.driver)

        def clickFirst(self):
            self.txtInvestorFirstName.click()
            waitForAngular(self.driver)

        def clickLast(self):
            self.txtInvestorLastName.click()
            waitForAngular(self.driver)

        def clickDOB(self):
            self.txtInvestorDOB.click()
            waitForAngular(self.driver)

        def clickSSN(self):
            self.txtInvestorSSN.click()
            waitForAngular(self.driver)

        def clickAddress1(self):
            self.txtInvestorAddress1.click()
            waitForAngular(self.driver)

        def clickAddress2(self):
            self.txtInvestorAddress2.click()
            waitForAngular(self.driver)

        def clickCity(self):
            self.txtInvestorCity.click()
            waitForAngular(self.driver)

        def clickState(self):
            self.ddlInvestorStateProvs.click()
            waitForAngular(self.driver)

        def clickZip(self):
            self.txtInvestorPostalCode.click()
            waitForAngular(self.driver)

        def clickPhone(self):
            self.txtInvestorPhone.click()
            waitForAngular(self.driver)

        def clickEmail(self):
            self.txtInvestorEmail.click()
            waitForAngular(self.driver)