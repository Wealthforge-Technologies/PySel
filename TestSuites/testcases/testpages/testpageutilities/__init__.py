from selenium import webdriver
from testutilities import Settings

DRIVER = None

def getOrCreateWebdriver():
    global DRIVER
    DRIVER = DRIVER or webdriver.Remote(
        command_executor=Settings.SELENIUMADDRESS,
        desired_capabilities=Settings.BROWSER)
    # current_width =  DRIVER.get_window_rect()['width']
    # current_height =  DRIVER.get_window_rect()['height']
    # print ([current_width, current_height])
    # print (Settings.WINDOWSIZE)
    # if [current_width, current_height] is not Settings.WINDOWSIZE: #set the window size if not done already
    #     print('Setting window size')
    #     DRIVER.set_window_size(Settings.WINDOWSIZE[0], Settings.WINDOWSIZE[1])

    return DRIVER


def setWindowSize(width=Settings.WINDOWSIZE[0],
                  height=Settings.WINDOWSIZE[1]):
    getOrCreateWebdriver().set_window_size(width, height)


def closeDriver():
    getOrCreateWebdriver().close()
