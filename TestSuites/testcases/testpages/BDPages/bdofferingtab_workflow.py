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
import os


class BDOfferingTabWork(BasePage):

    escrowAcctName = PageElement(id_='escrowNameInput')
    escrowAcctNumb = PageElement(id_='escrowNumberInput')
    escrowAcctBank = PageElement(id_='defaultBankSelect')

    statusPending = PageElement(css='[ng-click="setLocalStatus(\'OFFERING_PENDING\')"]')
    statusActive = PageElement(css='[ng-click="setLocalStatus(\'OFFERING_ACTIVE\')"]')
    statusDeactivate = PageElement(css='[ng-click="setLocalStatus(\'OFFERING_INACTIVE\')"]')
    statusPutInClosing = PageElement(css='[ng-click="setLocalStatus(\'OFFERING_IN_CLOSING\')"]')
    statusInClosing = PageElement(css='[ng-click="setLocalStatus(\'OFFERING_CLOSED\')"]')

    saveButton = PageElement(css='[ng-click="save()"]')

    def __init__(self):
        BasePage.__init__(self,
                          url='', #no defined useful url
                          title='') #no defined useful title

    def enterEscrowInfo(self, json):
        self.escrowAcctName.send_keys(json['escrowAcctName'])
        self.escrowAcctNumb.send_keys(json['escrowAcctNumb'])
        Select(self.escrowAcctBank).select_by_visible_text(json['escrowAcctBank'])

    def approveOffering(self):
        self.statusActive.click()

    def save(self):
        self.saveButton.click()
        waitForAngular(self.driver)


    def getDPOLink(self):
        pass