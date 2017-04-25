from selenium.webdriver.support.ui import WebDriverWait
from element import BasePageElement
from locators import MainPageLocators, QALoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchTextElement(BasePageElement):
  """This class gets the search text from the specified locator"""

  # The locator for search box where search string is entered
  locator = 'q'


class LoginEmailElement(BasePageElement):
  def __init__(self):
    self.locator = QALoginPageLocators.locators["login.email"]


class LoginPasswordElement(BasePageElement):
  def __init__(self):
    self.locator = QALoginPageLocators.locators["login.password"]

class LoginSubmitElement(BasePageElement):
  def __init__(self):
    self.locator = QALoginPageLocators.locators["login.submit"]


class BasePage(object):
  """Base class to initialize the base page that will be called from all pages"""

  def __init__(self, driver):
    self.driver = driver


class MainPage(BasePage):
  """Home page action methods come here. I.e. Python.org"""


class QALoginPage(BasePage):
  """QA login page action methods come here. I.e. https://qa1.wealthforge.org/login/#/"""

  def __init__(self, driver):
    self.driver = driver
    self.email = LoginEmailElement()
    self.password = LoginPasswordElement()
    self.btnsubmit = LoginSubmitElement()

  def is_title_matches(self):
    """Verifies that the hardcoded text "WF: Login" appears in page title"""
    return "WF: Login" in self.driver.title

  def submit(self, driver):
    try:
      element = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.ID, self.btnsubmit.locator))
      )
    finally:
      self.driver.find_element_by_id(self.btnsubmit.locator).click()


class SearchResultsPage(BasePage):
  """Search results page action methods come here"""

  def is_results_found(self):
    # Probably should search for this text in the specific page
    # element, but as for now it works fine
    return "No results found." not in self.driver.page_source
