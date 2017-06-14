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
    submitButton = PageElement(xpath="//button[contains(@ng-click,'save()')]")
    brandingDetails = PageElement(xpath="//div[contains(@ng-if, 'ORG_TYPE_ISS')]")



    def __init__(self):
        self.driver = getOrCreateWebdriver()
        waitForAngular(self.driver)
        self.actions = ActionChains(self.driver)


    #WARNING: issjson must match order and length of elementlist
    def fill_elements(self,issjson):
        waitForAngular(self.driver)
        assert len(self.elements) == len(issjson)
        for key, value in issjson.items():
            #self.actions.move_to_element(self.driver.find_element_by_id(key))
            elem = self.driver.find_element_by_id(key)
            self.driver.execute_script("arguments[0].scrollIntoView();", elem)
            wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, key)))
            if any(x in elem.get_attribute("id") for x in ["Drop","drop","BankSelect"]):
                Select(elem).select_by_visible_text(value)
                print ("...key:" + key + "\n...expected:" + value + "\n...value:" + Select(elem).all_selected_options[0].get_attribute("value"))
                assert value in Select(elem).all_selected_options[0].get_attribute("textContent")
            elif "color" in elem.get_attribute("id"):
                elem.clear()
                elem.send_keys("#")
                elem.send_keys(value)
                assert value in elem.get_attribute("value")
                print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
            else:
                elem.send_keys(value)
                print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
                assert value in elem.get_attribute("value")

    def verify_elements(self, issjson):
        waitForAngular(self.driver)
        assert len(self.elements) == len(issjson)
        print ("\n...Checking Issuer Data...\n\n")
        for key, value in issjson.items():
            elem = self.driver.find_element_by_id(key)
            # self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_id(key))
            # wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, key)))
            if any(x in elem.get_attribute("id") for x in ["Drop","drop","BankSelect"]):
                print ("...key:" + key + "\n...expected:" + value + "\n...value:" + Select(elem).all_selected_options[0].get_attribute("value"))
                assert value in Select(elem).all_selected_options[0].get_attribute("textContent")
            else:
                print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
                assert value in elem.get_attribute("value")

    def submit(self):
        assert self.submitButton is not None
        self.submitButton.click()
        waitForAngular(self.driver)
