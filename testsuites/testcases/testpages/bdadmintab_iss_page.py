from selenium.webdriver.support.ui import WebDriverWait
from .element import PageElement
from .basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .testpageutilities.waitforangular import waitForAngular
from selenium.webdriver.support import expected_conditions as EC


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


    #WARNING: issjson must match order and length of elementlist
    def fill_elements(self,issjson):
        assert len(self.elements) == len(issjson)
        for key, value in issjson.items():
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
                #print ("...key:" + key + "\n...expected:" + value + "\n...value:" + self.driver.find_element_by_id(key).get_attribute("value"))
                assert value in self.driver.find_element_by_id(key).get_attribute("value")

    def submit(self):
        assert self.submitButton is not None
        self.submitButton.click()
        waitForAngular(self.driver)
