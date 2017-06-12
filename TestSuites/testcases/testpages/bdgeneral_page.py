from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from .element import PageElement
from .basepage import BasePage
from .testpageutilities.waitforangular import waitForAngular
from selenium.webdriver.support import expected_conditions as EC
from .basepage import BasePage
from .testpageutilities import getOrCreateWebdriver


class BDGeneralPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/rad
    filter = PageElement(id_='search')
    hamburger = PageElement(id_='appDrawerToggle')
    currentUser = PageElement(xpath='//*[@id="bs-example-navbar-collapse-1"]/div/username/span/strong')
    dots = PageElement(css='#bs-example-navbar-collapse-1 > ul > li > a')
    support = PageElement(xpath='//*[@id="bs-example-navbar-collapse-1"]/ul/li/ul/li[1]/a')
    # TODO: Back to home page
    # TODO: Terms of Use
    # TODO: Privacy Statement
    logout = PageElement(css=("[ng-click*=logout()]"))

    def __init__(self):
        self.driver = getOrCreateWebdriver()
        self.expected_landing_url = "https://qa1.wealthforge.org/BD/#/rad"
        self.expected_title = "WF: Broker Dealer"

    def loadPagination(self):
        pass
        backOnePage = PageElement(css='icon ion-android-arrow-back')
        forwardOnePage = PageElement(css='icon ion-android-arrow-forward')

        numbPages = PageElement(css=("[ng-click*=logout()]"))[-1].__getattribute__("value")


