import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ..testpages.BDPages.bdhomepage import BDHomePage
from ..testcaseutilities.testinfo import TestInfo
from ..testcaseutilities.gmailaccessor import get_new_bd_user_password_reset_url
from ..testpages.BDPages.bdgeneral_page import BDGeneralPage
from ..testpages.BDPages.bdbanktab_page import BDBankTabPage

class TestBDAdmin(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()

    def test_bd_admin(self):
        bank = BDBankTabPage()

        bank.createBankBtn.click()
        # bank.bankFormElements['inputBankName'].click()



        bank.fill_elements(self.lookup.testbankinfo)

        bank.clickSave()



if __name__ == "__main__":
    unittest.main()
