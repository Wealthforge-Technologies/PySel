import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .testpages import bdloginpage
from .testpages.testpageutilities import waitforangular


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4445/wd/hub',
             desired_capabilities=DesiredCapabilities.CHROME)
        self.testinfo = TestInfo()
        self.testinfo.load_defaults()

    def test_login(self):
        login_page = BDLoginPage(self.driver)

        login_page.land()
        login_page.is_expected_landing_url()
        login_page.login(self.testinfo["CCO.email"],self.testinfo["CCO.password"])

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
