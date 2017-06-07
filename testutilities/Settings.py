from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def getdriver(self):
    return self.webdriver.Remote(
        command_executor='http://127.0.0.1:4445/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

def closeDriver(self):
    self.driver.close()
