from selenium import webdriver
from testutilities import Settings

DRIVER = None

def getOrCreateWebdriver():
    global DRIVER
    DRIVER = DRIVER or webdriver.Remote(
        command_executor=Settings.SELENIUMADDRESS,
        desired_capabilities=Settings.BROWSER)
    DRIVER.set_window_size(Settings.WINDOWSIZE[0], Settings.WINDOWSIZE[1])
    return DRIVER


def closeDriver():
    # getOrCreateWebdriver().close()
    DRIVER.close()
