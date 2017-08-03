from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement


class BDBankTabPage(BasePage):

    createBankBtn = PageElement(xpath="//nav[contains(@label,'Create Bank')]")
    saveButton = PageElement(xpath='//*[@id="bankForm"]/fieldset/div/div[2]/button')


    bankFormElements = {
        "inputBankName": PageElement(id_='inputBankName'),
        "inputDestinationRoutingNum": PageElement(id_='inputDestinationRoutingNum'),
        "inputOriginName": PageElement(id_='inputOriginName'),
        "inputOriginRoutingNum": PageElement(id_='inputOriginRoutingNum'),
        "inputCompany": PageElement(id_='inputCompany'),
        "inputClass": PageElement(id_='inputClass'),
        "inputAddress": PageElement(id_='inputAddress'),
        "inputAddressCont": PageElement(id_='inputAddressCont'),
        "inputCity": PageElement(id_='inputCity'),
        "inputState": PageElement(css='[ng-model="bank.state"]'),
        # "inputState": PageElement(css='//*[@id="bankForm"]/fieldset/div/div[1]/div[20]/select'),
        "inputZip": PageElement(id_='inputZip'),
        "inputPhone": PageElement(id_='inputPhone')
    }

    def __init__(self):
        BasePage.__init__(self,
                          url='/BD/#/banks',
                          title='WF: Broker Dealer')

    def fill_elements(self, bankJson):
        waitForAngular(self.driver)
        assert len(self.bankFormElements) == len(bankJson)
        for key, value in bankJson.items():
            elem = BDBankTabPage.bankFormElements[key].__get__(self, None, self.driver)  # JOHNNY IS A HACKER

            # move to the element.  If it is off the page then it will break.
            self.driver.execute_script("arguments[0].scrollIntoView();", elem)
            waitForAngular(self.driver)
            if key in ["inputClass","inputState"]:
                Select(elem).select_by_visible_text(value)
                # print ("...key:" + key + "\n...expected:" + value + "\n...value:" + Select(elem).all_selected_options[0].get_attribute("value"))
                assert value in Select(elem).all_selected_options[0].get_attribute("textContent")
            else:
                print('elem type=== '+ str(type(elem)))
                elem.send_keys(value)
                # elem.send_keys(value)
                # print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
                assert value in elem.get_attribute("value")

    def clickSave(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.saveButton)
        self.saveButton.click()
