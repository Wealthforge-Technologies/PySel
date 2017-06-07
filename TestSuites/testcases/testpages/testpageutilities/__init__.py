from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

DRIVER = None

def getOrCreateWebdriver():
    global DRIVER
    DRIVER = DRIVER or webdriver.Remote(
        command_executor='http://127.0.0.1:4445/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    return DRIVER

def closeDriver():
    DRIVER.close()
