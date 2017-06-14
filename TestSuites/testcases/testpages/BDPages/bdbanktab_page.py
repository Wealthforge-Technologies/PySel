from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver

class BDBankTabPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/banks
    create_bank_btn = PageElement(xpath="//nav[contains(@label,'Create Bank')]")
    elements = {}
    elements["inputBankName"] = PageElement(id_='inputBankName')
    elements["inputDestinationRoutingNum"] = PageElement(id_='inputDestinationRoutingNum')
    elements["inputOriginName"] = PageElement(id_='inputOriginName')
    elements["inputOriginRoutingNum"] = PageElement(id_='inputOriginRoutingNum')
    elements["inputCompany"] = PageElement(id_='inputCompany')
    elements["inputClass"] = PageElement(id_='inputClass') #dropdown
    elements["inputAddress"] = PageElement(id_='inputAddress')
    elements["inputAddressCont"] = PageElement(id_='inputAddressCont')
    elements["inputCity"] = PageElement(id_='inputCity')
    elements["inputState"] = PageElement(xpath='//*[@id="bankForm"]/fieldset/div/div[1]/div[20]/select') #dropdown, doesnt have an id
    elements["inputZip"] = PageElement(id_='inputZip')
    elements["inputPhone"] = PageElement(id_='inputPhone')




    def __init__(self):
        self.driver = getOrCreateWebdriver
        self.expected_landing_url = "https://qa1.wealthforge.org/BD/#/banks"
        self.expected_title = "WF: Broker Dealer"

    def is_expected_title(self):
        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(self.expected_title))
        finally:
            assert self.expected_title in self.driver.title
        waitForAngular(self.driver)


    def is_expected_landing_url(self):
        try:
            wait = WebDriverWait(self.driver, 5).until(
                lambda wait: self.driver.current_url == self.expected_landing_url)
        finally:
            assert self.expected_landing_url in self.driver.current_url
        waitForAngular(self.driver)


    def land(self):
        self.driver.get(self.expected_landing_url)
        waitForAngular(self.driver)

    def loadBanks(self):
        pass

    def getPagination(self):
        pass


    def fill_elements(self,bankJson):
        waitForAngular(self.driver)
        assert len(self.elements) == len(bankJson)
        for key, value in bankJson.items():
            #self.actions.move_to_element(self.driver.find_element_by_id(key))
            elem = self.driver.find_element_by_id(key)
            # move to the element.  If it is off the page then it will break.
            self.driver.execute_script("arguments[0].scrollIntoView();", elem)
            wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, key)))

            if any(x in elem.get_attribute("id") for x in ["inputClass","inputState"]):
                Select(elem).select_by_visible_text(value)
                # print ("...key:" + key + "\n...expected:" + value + "\n...value:" + Select(elem).all_selected_options[0].get_attribute("value"))
                assert value in Select(elem).all_selected_options[0].get_attribute("textContent")
            else:
                elem.send_keys(value)
                # print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
                assert value in elem.get_attribute("value")
