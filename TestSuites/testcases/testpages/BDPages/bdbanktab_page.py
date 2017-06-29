from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from selenium.webdriver.support.ui import Select


class BDBankTabPage(BasePage):

    createBankBtn = PageElement(xpath="//nav[contains(@label,'Create Bank')]")
    inputDestinationRoutingNum = PageElement(id_='inputDestinationRoutingNum')
    print(type(inputDestinationRoutingNum))
    bankFormElements = {}
    # bankFormElements['inputDestinationRoutingNum'] = PageElement(id_='inputDestinationRoutingNum')

    bankFormElements['inputDestinationRoutingNum'] = inputDestinationRoutingNum

    # bankFormElements = {
    #     "inputDestinationRoutingNum": PageElement(id_='inputDestinationRoutingNum'),
    #     "inputOriginName": PageElement(id_='inputOriginName'),
    #     "inputOriginRoutingNum": PageElement(id_='inputOriginRoutingNum'),
    #     "inputCompany": PageElement(id_='inputCompany'),
    #     "inputClass": PageElement(id_='inputClass'),
    #     "inputAddress": PageElement(id_='inputAddress'),
    #     "inputAddressCont": PageElement(id_='inputAddressCont'),
    #     "inputCity": PageElement(id_='inputCity'),
    #     "inputState": PageElement(css='[ng-model="bank.state"]'),
    #     # "inputState": PageElement(css='//*[@id="bankForm"]/fieldset/div/div[1]/div[20]/select'),
    #
    #     "inputZip": PageElement(id_='inputZip'),
    #     "inputPhone": PageElement(id_='inputPhone')
    # }

    def __init__(self):
        BasePage.__init__(self,
                          url='/BD/#/banks',
                          title='WF: Broker Dealer')
        # self.bankFormElements = {
        #         "inputDestinationRoutingNum": PageElement(id_='inputDestinationRoutingNum'),
        #         "inputOriginName": PageElement(id_='inputOriginName'),
        #         "inputOriginRoutingNum": PageElement(id_='inputOriginRoutingNum'),
        #         "inputCompany": PageElement(id_='inputCompany'),
        #         "inputClass": PageElement(id_='inputClass'),
        #         "inputAddress": PageElement(id_='inputAddress'),
        #         "inputAddressCont": PageElement(id_='inputAddressCont'),
        #         "inputCity": PageElement(id_='inputCity'),
        #         "inputState": PageElement(css='[ng-model="bank.state"]'),
        #         # "inputState": PageElement(css='//*[@id="bankForm"]/fieldset/div/div[1]/div[20]/select'),
        #
        #         "inputZip": PageElement(id_='inputZip'),
        #         "inputPhone": PageElement(id_='inputPhone')
        #         }

    def fill_elements(self, bankJson):
        waitForAngular(self.driver)
        # assert len(self.bankFormElements) == len(bankJson)
        # for key, value in bankJson.items():
        #     #self.actions.move_to_element(self.driver.find_element_by_id(key))
        #     print(self.bankFormElements[key])
        #     elem = self.bankFormElements[key]
        #
        #     # move to the element.  If it is off the page then it will break.
        #     # self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        #     waitForAngular(self.driver)
        #     print(key)
        #     if key in ["inputClass","inputState"]:
        #         pass
        #         # Select(elem).select_by_visible_text(value)
        #         # # print ("...key:" + key + "\n...expected:" + value + "\n...value:" + Select(elem).all_selected_options[0].get_attribute("value"))
        #         # assert value in Select(elem).all_selected_options[0].get_attribute("textContent")
        #     else:
        #         elem.send_keys(value)
        #         # print ("...key:" + key + "\n...expected:" + value + "\n...value:" + elem.get_attribute("value"))
        #         assert value in elem.get_attribute("value")
        print(type(self.inputDestinationRoutingNum))

        # self.inputDestinationRoutingNum.send_keys(bankJson['inputDestinationRoutingNum'])
        self.bankFormElements['inputDestinationRoutingNum'].send_keys(bankJson['inputDestinationRoutingNum'])