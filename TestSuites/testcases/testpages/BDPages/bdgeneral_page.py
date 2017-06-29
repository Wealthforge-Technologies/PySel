from ..element import PageElement
from ..basepage import BasePage
from selenium.webdriver.common.keys import Keys


class BDGeneralPage(BasePage):
    filterField = PageElement(id_='search')
    itemsPerPage = PageElement(css='[ng-model="pageSize"]')
    hamburger = PageElement(id_='appDrawerToggle')
    currentUser = PageElement(xpath='//*[@id="bs-example-navbar-collapse-1"]/div/username/span/strong')
    dots = PageElement(css='#bs-example-navbar-collapse-1 > ul > li > a')
    support = PageElement(xpath='//*[@id="bs-example-navbar-collapse-1"]/ul/li/ul/li[1]/a')
    logoutButton = PageElement(css='[ng-click="logout()"]')
    nextPageButton = PageElement(css='ng-click="setCurrent(pagination.current + 1)"')
    # TODO: Back to home page
    # TODO: Terms of Use
    # TODO: Privacy Statement

    def __init__(self):
        BasePage.__init__(self)

    def getNumbPages(self):
        return self.driver.execute_script('return document.querySelectorAll(\'[ng-click*="setCurrent(pageNumber)"]\').length')

    def setItemsPerPage(self, n):
        self.itemsPerPage.clear()
        self.itemsPerPage.send_keys(str(n))

    def clickNextPage(self):
        self.nextPageButton.send_keys(Keys.NULL)
        self.nextPageButton.click()

    def logout(self):
        self.dots.click()
        self.logoutButton.click()

    def filter(self, txt):
        self.filterField.send_keys(txt)

    # def getCurrentUser(self):
    #     assert self.currentUser is not None, 'Could not find Element!'
    #     return self.currentUser.get_attribute("textContent").lstrip()