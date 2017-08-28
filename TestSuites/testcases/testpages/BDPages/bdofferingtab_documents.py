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


class BDOfferingTabDocs(BasePage):

    saveButton = PageElement(css='[ng-click="saveDocs()"]')
    backButton = PageElement(css='[ng-click="back()"]')
    uploadButton = PageElement(id_='fileBox')

    def __init__(self):
        BasePage.__init__(self,
                          url='', #no defined useful url
                          title='') #no defined useful title

    def uploadDefaultDocs(self):

        # Due Diligence
        self.uploadButton.send_keys((os.getcwd()+'/testcases/testcaseutilities/documents/Test Document.pdf'))
        waitForAngular(self.driver)
        dropdowns = self.driver.find_elements_by_css_selector('[ng-model="record.folderType"]')
        Select(dropdowns[0]).select_by_visible_text('Due Diligence')

        # Investor Signatory Document - Individual
        self.uploadButton.send_keys((os.getcwd()+'/testcases/testcaseutilities/documents/Test Document.pdf'))
        waitForAngular(self.driver)
        dropdowns = self.driver.find_elements_by_css_selector('[ng-model="record.folderType"]')
        Select(dropdowns[1]).select_by_visible_text('Investor Signatory Document - Individual')

        # Investor Signatory Document - Entity
        self.uploadButton.send_keys((os.getcwd()+'/testcases/testcaseutilities/documents/Test Document.pdf'))
        waitForAngular(self.driver)
        dropdowns = self.driver.find_elements_by_css_selector('[ng-model="record.folderType"]')
        Select(dropdowns[2]).select_by_visible_text('Investor Signatory Document - Entity')

        #TODO: change to a document with a spouse signature field
        # Investor Signatory Document - Married
        self.uploadButton.send_keys((os.getcwd()+'/testcases/testcaseutilities/documents/Test Document.pdf'))
        waitForAngular(self.driver)
        dropdowns = self.driver.find_elements_by_css_selector('[ng-model="record.folderType"]')
        Select(dropdowns[3]).select_by_visible_text('Investor Signatory Document - Married')

    def uploadMultipleDocs(self):
        #TODO: might be possible, check:
        # https://stackoverflow.com/questions/23955430/webdriverupload-multiple-files
        pass

    def save(self):
        self.saveButton.click()
        waitForAngular(self.driver)


