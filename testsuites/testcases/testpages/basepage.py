from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""


    # DRIVER = None
    #
    # def getOrCreateWebdriver(self):
    #     global DRIVER
    #     DRIVER = DRIVER or webdriver.Remote(
    #         command_executor='http://127.0.0.1:4445/wd/hub',
    #         desired_capabilities=DesiredCapabilities.CHROME)
    #     return DRIVER
    #
    # def closeDriver(self):
    #     DRIVER.close()
