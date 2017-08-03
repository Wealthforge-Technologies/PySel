from selenium.webdriver.support.ui import WebDriverWait
from ..element import PageElement
from ..basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ..testpageutilities.waitforangular import waitForAngular
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ..testpageutilities import getOrCreateWebdriver


class BDOfferingTabInfo(BasePage):
    offeringFormElements = {
        'offeringTitle': PageElement(css='[ng-model="offering.title"]'),
        'regTypeDropdown': PageElement(css='[name="regulationType"]'),
        'dateStart': PageElement(id_='dateStart'),
        'dateEnd': PageElement(id_='dateEnd'),
        'minOfferRaise': PageElement(css='[ng-model="offering.minRaise"]'),
        'maxOfferRaise': PageElement(css='[ng-model="offering.maxRaise"]'),
    }
    termFormElements = {
        'termType': PageElement(css='[name="securityType"]'),  # Dropdown
        'classTitle': PageElement(css='[ng-model="offering.terms.title"]'),
        'minInvestment': PageElement(css='[ng-model="offering.terms.minInvestment"]'),
        'minTermRaise': PageElement(css='[ng-model="offering.terms.minRaise"]'),
        'maxTermRaise': PageElement(css='[ng-model="offering.terms.maxRaise"]'),
        'price': PageElement(css='[ng-model="offering.terms.price"]'),  # note this changes names depending on the termType
        'notesIssued': PageElement(css='[ng-model="offering.terms.issued"]'),
    }

    # situational fields based on termType
    interestRate = PageElement(css='[ng-model="offering.terms.interestRate"]')
    maturityMonths = PageElement(css='[ng-model="offering.terms.maturity"]')
    paymentFreqDropdown = PageElement(css='[name="paymentFrequency"]')  # Dropdown
    conversionRatio = PageElement(css='ng-model="offering.terms.discount"')

    # Payment Types
    paymentTypesRadio = PageElement(css='[ng-model="offering.metadata.paymentOptions[type.code]"]')  # all of the radio buttons

    continueButton = PageElement(css='ng-click="saveOffering()"')

    def __init__(self):
        BasePage.__init__(self,
                          url='', #no defined useful url
                          title='') #no defined useful title

    def setRegType(self, type):
        regTypeElem = self.offeringFormElements['regTypeDropdown'].__get__(self, None, self.driver)
        if type is 'RegB':
            Select(regTypeElem).select_by_visible_text('Regulation D Exemption 506(b)')
        if type is 'RegC':
            Select(regTypeElem).select_by_visible_text('Regulation D Exemption 506(c)')


    #TODO: make this dynamic to select any date (difficult)
    # There are several calendars loaded but hidden in the DOM. This finds the active one
    def setDates(self):
        dateStart = self.offeringFormElements['dateStart'].__get__(self, None, self.driver)
        dateEnd = self.offeringFormElements['dateEnd'].__get__(self, None, self.driver)

        dateStart.click()
        activeCalendar = self.driver.find_element_by_css_selector("div[id^='dtp_']:not(.hidden)")
        prevYear = activeCalendar.find_element_by_css_selector('.dtp-select-year-before')
        okButton = activeCalendar.find_element_by_css_selector('.dtp-btn-ok')

        prevYear.click()
        okButton.click()

        dateEnd.click()
        activeCalendar = self.driver.find_element_by_css_selector("div[id^='dtp_']:not(.hidden)")
        nextYear = activeCalendar.find_element_by_css_selector('.dtp-select-year-after')
        okButton = activeCalendar.find_element_by_css_selector('.dtp-btn-ok')

        nextYear.click()
        okButton.click()


    def fill_offering_fields(self,json):
        waitForAngular(self.driver)
        assert len(self.offeringFormElements) == len(json)
        for key, value in json.items():
            elem = self.offeringFormElements[key].__get__(self, None, self.driver)  # JOHNNY IS A HACKER
            self.driver.execute_script("arguments[0].scrollIntoView();", elem)

            #Other Elements
            if key in ["regTypeDropdown","inputState"]:
                self.setRegType(json['regTypeDropdown'])

            elif key in ["dateStart","dateEnd"]:
                pass

            else:
                elem.send_keys(value)
                print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
                # assert value in elem.get_attribute("value")
        self.setDates()

    def fill_term_fields(self, defaultJson, otherJson):

        # Default Fields on all Term Types:
        waitForAngular(self.driver)
        for key, value in defaultJson.items():
            if key is not 'paymentTypes':

                elem = self.termFormElements[key].__get__(self, None, self.driver)  # JOHNNY IS A HACKER
                self.driver.execute_script("arguments[0].scrollIntoView();", elem)


                #Dropdowns
                if key in ["termType"]:
                    Select(elem).select_by_visible_text(value)
                    print ("...key:" + key + "\n...expected:" + value + "\n...value:" + Select(elem).all_selected_options[0].get_attribute("value"))
                    assert value in Select(elem).all_selected_options[0].get_attribute("textContent")
                else:
                    elem.send_keys(value)
                    print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
                    assert value in elem.get_attribute("value")
            else:
                self.fill_payment_types(defaultJson['paymentTypes'])



        # Other fields, some are there when you select certain Term Types
        if defaultJson['termType'] is 'Debenture':
            self.interestRate.sendKeys(otherJson['interestRate'])
            self.maturityMonths.sendKeys(otherJson['maturityMonths'])
            Select(self.paymentFreqDropdown).select_by_visible_text(otherJson['paymentFreqDropdown'])
        elif defaultJson['termType'] is 'Common':
            pass  # no extra fields for Common
        elif defaultJson['termType'] is 'Preferred':
            self.interestRate.sendKeys(otherJson['interestRate'])  # The text says Preferred Return but the type is interestRate
        elif defaultJson['termType'] is 'Convertible Note':
            self.interestRate.sendKeys(otherJson['interestRate'])
            self.conversionRatio.sendKeys(otherJson['conversionRatio'])
            self.maturityMonths.sendKeys(otherJson['maturityMonths'])
            Select(self.paymentFreqDropdown).select_by_visible_text(otherJson['paymentFreqDropdown'])
        elif defaultJson['termType'] is 'Interests':
            self.interestRate.sendKeys(otherJson['interestRate'])
            Select(self.paymentFreqDropdown).select_by_visible_text(otherJson['paymentFreqDropdown'])
        elif defaultJson['termType'] is 'Shares':
            pass  # no extra fields for Shares

    def fill_payment_types(self, bits):
        '''
        Clicks the appropriate payment options
        :param bits: bitwise representation of the payment options
        '''
        paymentTypes = self.driver.find_elements_by_css_selector('[ng-model="offering.metadata.paymentOptions[type.code]"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", paymentTypes[0])

        for x in range(bits.bit_length()):
            paymentTypes[x].click()


    def submit(self):
        self.continueButton.click()
        waitForAngular(self.driver)


