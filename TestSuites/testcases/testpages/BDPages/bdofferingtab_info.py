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
    paymentFreqDropdown= PageElement(css='[name="paymentFrequency"]') #Dropdown

    # Payment Types
    paymentTypesRadio = PageElement(css='[ng-model="offering.metadata.paymentOptions[type.code]"]')  # all of the radio buttons

    # Calendar Buttons
    activeCalendar = PageElement(css='.dtp-time div:not(.hidden)')
    prevYear = PageElement(css='.dtp-select-year-before')
    nextYear = PageElement(css='.dtp-select-year-after')
    calendarOk = PageElement(css='.dtp-btn-ok')


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


    #TODO: make this not always do the same thing
    # There are several calendars loaded but hidden in the DOM. This finds the active one
    def setDates(self):
        dateStart = self.offeringFormElements['dateStart'].__get__(self, None, self.driver)
        dateEnd = self.offeringFormElements['dateEnd'].__get__(self, None, self.driver)


        dateStart.click()

        # Calendar Buttons
        activeCalendar = self.driver.find_element_by_css_selector('.dtp-time div:not(.hidden)')
        prevYear = activeCalendar.find_element_by_css_selector('.dtp-select-year-before')
        nextYear = activeCalendar.find_element_by_css_selector('.dtp-select-year-after')
        okButton = activeCalendar.find_element_by_css_selector('.dtp-btn-ok')

        prevYear.click()
        okButton.click()




    def fill_elements(self,json):
        waitForAngular(self.driver)
        assert len(self.offeringFormElements) == len(json)
        for key, value in json.items():
            elem = self.offeringFormElements[key].__get__(self, None, self.driver)  # JOHNNY IS A HACKER
            self.driver.execute_script("arguments[0].scrollIntoView();", elem)

            #Other Elements
            if key in ["regTypeDropdown","inputState"]:
                self.setRegType(json['regTypeDropdown'])

            #Dropdowns
            elif key in ["____","____"]:
                Select(elem).select_by_visible_text(value)
                print ("...key:" + key + "\n...expected:" + value + "\n...value:" + Select(elem).all_selected_options[0].get_attribute("value"))
                assert value in Select(elem).all_selected_options[0].get_attribute("textContent")
            else:
                elem.send_keys(value)
                print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
                assert value in elem.get_attribute("value")

    # def verify_elements(self, json):
    #     waitForAngular(self.driver)
    #     assert len(self.offeringFormElements) == len(json)
    #     print ("\n...Checking Offering Data...\n\n")
    #     for key, value in json.items():
    #         elem = self.offeringFormElements[key].__get__(self, None, self.driver)  # JOHNNY IS A HACKER
    #         self.driver.execute_script("arguments[0].scrollIntoView();", elem)
    #         if key in ["inputClass","inputState"]:
    #             print ("...key:" + key + "\n...expected:" + value + "\n...value:" + Select(elem).all_selected_options[0].get_attribute("value"))
    #             assert value in Select(elem).all_selected_options[0].get_attribute("textContent")
    #         else:
    #             print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
    #             assert value in elem.get_attribute("value")

    def submit(self):
        assert self.continueButton is not None
        self.continueButton.click()
        waitForAngular(self.driver)


