from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .element import PageElement
from .testpageutilities.waitforangular import waitForAngular
from .basepage import BasePage

class NWHomePage(BasePage):
    # """QA login page action methods come here. I.e. https://qa1.wealthforge.org/login/#/"""
    # url = "https://qa1.wealthforge.org/login/#/"
    # email = PageElement(id_='username')
    # password = PageElement(id_='password')
    # btnLogin = PageElement(id_='btnLogin')

    # Page elements:
    "Head:"
    head_navSpace = PageElement(id_='navSpace') # NW/#/
    head_wfLogo = PageElement(id_='wfLogo')  # NW/#/
    navbarCollapse_IP = PageElement(id_='bs-example-navbar-collapse-1') # NW/#/
    head_navMenu = PageElement(id_='navMenu') # NW/#/
    # hamburger = PageElement(id_='appDrawerToggle') # NW/#/ TODO (doublecheck/refactor)
    head_hamburger = PageElement(id_='dropdown1') # NW/#/

    "Main:"
    main_search = PageElement(id_='search') # NW/#/
    main_industrySelect = PageElement(id_='select-options-74a040eb-a54e-a516-6cb5-464acc5e5e2d') # NW/#/
    main_itemsPerPage = PageElement(id_='pageSize') # NW/#/
    # TODO - Paginations!

    "Footer:"
    # TODO define items for bottom section(s)

    # 'Typical' tests
    def __init__(self, driver):
        self.driver = driver
        self.expected_landing_url = "https://qa1.wealthforge.org/NW/#/showcase"
        self.expected_title = "WF: Network" #TODO 'wtf this won't test'
        # self.tsViewDetails = None

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

    # NW specific tests   'IP' = 'if present' ----------------------------------

    # Basic HTML elements as defined above:
    def head_navSpace_IP(self):
        waitForAngular(self.driver)
        assert self.driver.find_element_by_id('navSpace') is not None
        #print("hello world")

    def head_wfLogo_IP(self):
        waitForAngular(self.driver)
        assert self.driver.find_element_by_id('wfLogo') is not None

    def navbarCollapse_IP(self):
        waitForAngular(self.driver)
        assert self.driver.find_element_by_id('bs-example-navbar-collapse-1') is not None

    def head_navMenu_IP(self):
        waitForAngular(self.driver)
        assert self.driver.find_element_by_id('navMenu') is not None

    def head_dropdown1_IP(self):
        waitForAngular(self.driver)
        assert self.driver.find_element_by_id('dropdown1') is not None

    def main_search_IP(self):
        waitForAngular(self.driver)
        assert self.driver.find_element_by_id('search') is not None

    # def main_industrySelect_IP(self):
    #     waitForAngular(self.driver)
    #     assert self.driver.find_element_by_id('select-options-74a040eb-a54e-a516-6cb5-464acc5e5e2d') is not None

    def main_itemsPerPage_IP(self):
        waitForAngular(self.driver)
        assert self.driver.find_element_by_id('pageSize') is not None


    # Tombstone & pagination testing?? TODO
    # def tombstonetest(self):
    #     waitForAngular(self.driver)
    #     assert self.driver
