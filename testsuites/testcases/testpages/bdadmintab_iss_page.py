from selenium.webdriver.support.ui import WebDriverWait
from .element import PageElement
from .basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .testpageutilities.waitforangular import waitForAngular
from selenium.webdriver.support import expected_conditions as EC


import time


class BDAdminTabIssPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/rad
    elements = {}
    elements["displayNameInput"] = PageElement(id_='displayNameInput')
    elements["address1Input"] = PageElement(id_='address1Input')
    elements["address2Input"] = PageElement(id_='address2Input')
    elements["cityInput"] = PageElement(id_='cityInput')
    elements["stateDrop"] = PageElement(id_='stateDrop')
    elements["zipInput"] = PageElement(id_='zipInput')
    elements["phoneInput"] = PageElement(id_='phoneInput')
    elements["logoUrlInput"] = PageElement(id_='logoUrlInput')
    elements["urlInput"] = PageElement(id_='urlInput')
    elements["colorPrimaryInput"] = PageElement(id_='colorPrimaryInput')
    elements["colorSecondaryInput"] = PageElement(id_='colorSecondaryInput')
    elements["legalInput"] = PageElement(id_='legalInput')
    elements["corpTypeSelect"] = PageElement(id_='corpTypeSelect')
    elements["incorpStateDrop"] = PageElement(id_='incorpStateDrop')
    elements["pocInput"] = PageElement(id_='pocInput')
    elements["poctInput"] = PageElement(id_='poctInput')
    elements["pocEmailInput"] = PageElement(id_='pocEmailInput')
    elements["issBankSelect"] = PageElement(id_='issBankSelect')
    elements["taxInput"] = PageElement(id_='taxInput')
    btnCancel = PageElement(id_='btnCancel')
    submitButton = PageElement(xpath="//button[contains(@ng-click,'submit()')]")



    def __init__(self, driver):
        self.driver = driver
        waitForAngular(self.driver)

    def add_role(self, role):
        assert self.rolesDropdown is not None
        Select(self.rolesDropdown).select_by_visible_text(role)
        self.rolesAdd.click()
        waitForAngular(self.driver)

    #WARNING: issjson must match order and length of elementlist
    def fill_elements(self,issjson):
        assert len(self.elements) == len(issjson)
        # for element, value in zip(self.elementlist, issjson.values()):
        #     if "Drop" in element.get_attribute("id") or "drop" in element.get_attribute("id"):
        #         Select(element).select_by_visible_text(value)
        #     else:
        #         assert element is not None
        #         element.send_keys(value)
        #         assert value in element.get_attribute("value")
        for key, value in issjson.items():
            #waitForAngular(self.driver)
            try:
                wait = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.ID, key))
                    )
            finally:
                assert self.driver.find_element_by_id(key).is_enabled()
            if any(x in self.driver.find_element_by_id(key).get_attribute("id") for x in ["Drop","drop","BankSelect"]):
                Select(self.driver.find_element_by_id(key)).select_by_visible_text(value)
            elif "color" in self.driver.find_element_by_id(key).get_attribute("id"):
                self.driver.find_element_by_id(key).clear()
                self.driver.find_element_by_id(key).send_keys("#")
                self.driver.find_element_by_id(key).send_keys(value)
                assert value in self.driver.find_element_by_id(key).get_attribute("value")
            else:
                self.driver.find_element_by_id(key).click()
                self.driver.find_element_by_id(key).send_keys(value)
                print ("...key:" + key + "\n...expected:" + value + "\n...value:" + self.driver.find_element_by_id(key).get_attribute("value"))
                assert value in self.driver.find_element_by_id(key).get_attribute("value")
            #time.sleep(.5)





    def enter_info(self, first, last, email):
        assert self.firstName is not None
        self.firstName.send_keys(first)
        assert first in self.firstName.get_attribute("value")

        assert self.lastName is not None
        self.lastName.send_keys(last)
        assert last in self.lastName.get_attribute("value")

        assert self.email is not None
        self.email.send_keys(email)
        assert email in self.email.get_attribute("value")


    def submit(self):
        assert self.submitButton is not None
        self.submitButton.click()
        waitForAngular(self.driver)


    def first_name_should_be(self, expected_firstname):
        waitForAngular(self.driver)
        assert self.firstName is not None
        assert expected_firstname in self.firstName.get_attribute("value")

    def last_name_should_be(self, expected_lastname):
        waitForAngular(self.driver)
        assert self.lastName is not None
        assert expected_lastname in self.lastName.get_attribute("value")

    def email_should_be(self, expected_email):
        waitForAngular(self.driver)
        assert self.email is not None
        assert expected_email in self.email.get_attribute("value")


    def roles_should_contain(self, role):
        waitForAngular(self.driver)
        assert self.driver.find_elements_by_xpath("//li[contains(@ng-repeat,'roles')]") is not None
        for eachrole in self.driver.find_elements_by_xpath("//li[contains(@ng-repeat,'roles')]"):
            if role in eachrole.get_attribute("textContent"):
                assert True
                return
        assert False
