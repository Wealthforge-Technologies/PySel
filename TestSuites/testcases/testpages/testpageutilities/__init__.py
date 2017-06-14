from selenium import webdriver
from testutilities import Settings

DRIVER = None

def getOrCreateWebdriver():
    global DRIVER
    DRIVER = DRIVER or webdriver.Remote(
        command_executor=Settings.seleniumAddress,
        desired_capabilities=Settings.browser)
    DRIVER.set_window_size(Settings.windowSize[0], Settings.windowSize[1])
    return DRIVER


def closeDriver():
    # getOrCreateWebdriver().close()
    DRIVER.close()
