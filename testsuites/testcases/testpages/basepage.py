from selenium.webdriver.support.ui import WebDriverWait
from .testpageutilities.waitforangular import waitForAngular
from selenium.webdriver.support import expected_conditions as EC
from .testpageutilities import getOrCreateWebdriver
from testutilities import Settings


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, url='', title=''):
        self.driver = getOrCreateWebdriver()
        self.url = Settings.ENVIRONMENT + url
        self.title = title

    def is_expected_landing_url(self):
        if self.url is Settings.ENVIRONMENT:
            print('ERROR: URL not defined, can\'t check expected URL')
        else:
            try:
                wait = WebDriverWait(self.driver, 2).until(
                    lambda wait: self.url in self.driver.current_url)
            finally:
                assert self.url in self.driver.current_url, 'URLs do not match!'
            waitForAngular(self.driver)

    def is_expected_title(self):
        """Verifies that the hardcoded text "WF: Investor Platform" appears in page title"""
        if self.title is '':
            print('ERROR: Title not defined, can\'t check expected Title')
        else:
            try:
                wait = WebDriverWait(self.driver, 5).until(
                    EC.title_contains(self.title))
            finally:
                assert self.title in self.driver.title
            waitForAngular(self.driver)

    def land(self):
        if self.url is '':
            print('ERROR: Can\'t go to page: No URL Set')
        else:
            self.driver.get(self.url)
