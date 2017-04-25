from selenium.webdriver.support.ui import WebDriverWait
from element import PageElement
from locators import MainPageLocators, QALoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# class LoginEmailElement(PageElement):
#   def __init__(self, context=False, **kwargs):
#         if not kwargs:
#             raise ValueError("Please specify a locator")
#         if len(kwargs) > 1:
#             raise ValueError("Please specify only one locator")
#         k, v = next(iter(kwargs.items()))
#         self.locator = (_LOCATOR_MAP[k], v)
#         self.has_context = bool(context)
#
# class LoginPasswordElement(PageElement):
#   def __init__(self, context=False, **kwargs):
#         if not kwargs:
#             raise ValueError("Please specify a locator")
#         if len(kwargs) > 1:
#             raise ValueError("Please specify only one locator")
#         k, v = next(iter(kwargs.items()))
#         self.locator = (_LOCATOR_MAP[k], v)
#         self.has_context = bool(context)
#
# class LoginSubmitElement(PageElement):
#   def __init__(self, context=False, **kwargs):
#         if not kwargs:
#             raise ValueError("Please specify a locator")
#         if len(kwargs) > 1:
#             raise ValueError("Please specify only one locator")
#         k, v = next(iter(kwargs.items()))
#         self.locator = (_LOCATOR_MAP[k], v)
#         self.has_context = bool(context)


class BasePage(object):
  """Base class to initialize the base page that will be called from all pages"""

  def __init__(self, driver):
    self.driver = driver


class MainPage(BasePage):
  """Home page action methods come here. I.e. Python.org"""


class QALoginPage(BasePage):
  """QA login page action methods come here. I.e. https://qa1.wealthforge.org/login/#/"""
  url = "https://qa1.wealthforge.org/login/#/"
  email = PageElement(id_='username')
  password = PageElement(id_='password')

  def __init__(self, driver):
    self.driver = driver

  def is_title_matches(self):
    """Verifies that the hardcoded text "WF: Login" appears in page title"""
    assert "WF: Login" in self.driver.title

  def submit(self):
    try:
      wait = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_id('btnLogin'))
    finally:
      self.driver.find_element_by_id('btnLogin').click()


class SearchResultsPage(BasePage):
  """Search results page action methods come here"""

  def is_results_found(self):
    # Probably should search for this text in the specific page
    # element, but as for now it works fine
    return "No results found." not in self.driver.page_source
