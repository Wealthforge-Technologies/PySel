from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver

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
    def __init__(self):
        self.driver = getOrCreateWebdriver()
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

    # NW specific tests   IP = IsPresent: --------------------------------------
    def head_navSpace_IP(self):
        try:
            self.driver.find_element(by=id, value='navSpace')
            #print("hello found!")
        except NoSuchElementException as e:
            return False
        return True

    def head_wfLogo_IP(self):
        try:
            self.driver.find_element(by=id, value='wfLogo')
        except NoSuchElementException as e:
            return False
        return True

    def head_navMenu_IP(self):
        try:
            self.driver.find_element(by=id, value='navMenu')
        except NoSuchElementException as e:
            return False
        return True

    def head_dropdown1_IP(self):
        try:
            self.driver.find_element(by=id, value='dropdown1')
        except NoSuchElementException as e:
            return False
        return True

    def main_search_IP(self):
        try:
            self.driver.find_element(by=id, value='search')
        except NoSuchElementException as e:
            return False
        return True

    def main_industrySelect_IP(self):
        try:
            self.driver.find_element(by=id, value='select-options-74a040eb-a54e-a516-6cb5-464acc5e5e2d')
        except NoSuchElementException as e:
            return False
        return True

    def main_itemsPerPage_IP(self):
        try:
            self.driver.find_element(by=id, value='pageSize')
        except NoSuchElementException as e:
            return False
        return True
