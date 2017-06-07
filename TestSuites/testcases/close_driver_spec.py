import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .testpages.bdloginpage import BDLoginPage
from .testpages.bdhomepage import BDHomePage
from .testcaseutilities.testinfo import TestInfo
from .testpages.testpageutilities import closeDriver

class CloseDriver(unittest.TestCase):


    def test_close(self):
        closeDriver()





if __name__ == "__main__":
    unittest.main()
