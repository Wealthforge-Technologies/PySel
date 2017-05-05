from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from .element import PageElement
from .basepage import BasePage
from .testpageutilities.waitforangular import waitForAngular

class BDAdminTabPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/rad
    search = PageElement(id_='search')
    hamburger = PageElement(id_='appDrawerToggle')
    dots = PageElement(css='#bs-example-navbar-collapse-1 > ul > li > a')



    def __init__(self, driver):
        self.driver = driver
        self.expected_landing_url = "https://qa1.wealthforge.org/BD/#/rad"
        self.expected_title = "WF: Broker Dealer"
        self.treespace = {}

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

    def loadtreespace(self):
        # elements = self.driver.find_elements_by_xpath("//*[contains(@href,'#/rad/editOrg?id=')]")
        # //div[@id = 'content']/descendant::text()[not(ancestor::div/@class='infobox')]
        elements = self.driver.find_elements_by_xpath("//*[contains(@href,'#/rad/editOrg?id=')]")
        #elements = self.driver.find_elements_by_xpath("//*[contains(@href,'#/rad/edit')]")
        for element in self.driver.find_elements_by_xpath("//div[contains(@href,'#/rad/editUser?id=')]"):
            elements.append(element)
        for element in elements:
            self.treespace[element.get_attribute("textContent").lstrip()] = element
        print("..." + str(len(self.treespace)) + "...\n")
        for thing in self.treespace:
            print(thing+"..\n")
