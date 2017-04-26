from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass


class QALoginPageLocators(object):
    """A class for QA Login Page locators. All QA Login Page locators should come here"""
    # EMAIL = (By.ID, 'username')
    # PASSWORD = (By.ID, 'password')
    # LOGIN_BUTTON = (By.ID, 'btnLogin')
    locators = {}
    locators["login.email"] = "username"
    locators["login.password"] = "password"
    locators["login.submit"] = "btnLogin"
