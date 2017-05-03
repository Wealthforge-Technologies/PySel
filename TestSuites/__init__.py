from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

DRIVER = None

def driver():
    global DRIVER
    DRIVER = DRIVER or webdriver.Remote(
         command_executor='http://localhost:4445/wd/hub',
         desired_capabilities=DesiredCapabilities.CHROME)
    return DRIVER
