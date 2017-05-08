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

    def load_treenodes(self):
        # elements = self.driver.find_elements_by_xpath("//*[contains(@href,'#/rad/editOrg?id=')]")
        # //div[@id = 'content']/descendant::text()[not(ancestor::div/@class='infobox')]
        orgs = self.driver.find_elements_by_xpath("//*[contains(@href,'#/rad/editOrg?id=')]")
        orgsoptions = []
        for org in orgs:
            idstring = str(org.get_attribute("href")).split("?id=")[1]
            print(idstring)
            containsidstring = "//a[contains(@href,'" + idstring + "')]"
            orgsoptions.append(self.driver.find_elements_by_xpath(containsidstring))
        orgsdots = self.driver.find_elements_by_xpath("//div[contains(@href,'#/rad/editOrg?id=')]/../../a")

        assert len(orgs) == len(orgsdots) == len(orgsoptions)
        print("\n Lengths good.\n")

        for treenode in zip(orgs, orgsdots, orgsoptions):
            self.treespace[treenode[0].get_attribute("textContent").lstrip().split('\n')[1].lstrip()] = treenode
        #elements = self.driver.find_elements_by_xpath("//*[contains(@href,'#/rad/edit')]")
        users = self.driver.find_elements_by_xpath("//div[contains(@href,'#/rad/editUser?id=')]")
        for user in users:
            self.treespace[user.get_attribute("textContent").lstrip().split('\n')[0]] = user
        print(self.treespace)
