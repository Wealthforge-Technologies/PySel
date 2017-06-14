from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..element import PageElement
from ..testpageutilities.waitforangular import waitForAngular
from ..basepage import BasePage
from ..testpageutilities import getOrCreateWebdriver


class IPEmploymentStatusPage(BasePage):
    btnBack = PageElement(id_='Back')
    btnContinue = PageElement(id_='btnContinue')
    employStatus = PageElement(id_='ddlInvestorEmploymentStatus')
    otherOpportYes = PageElement(id_='rbOtherOpportunitiesYes')
    otherOpportNo = PageElement(id_='rbOtherOpportunitiesNo')

    def __init__(self):
        self.driver = getOrCreateWebdriver()
        self.expected_landing_url = "https://qa1.wealthforge.org/IP/#/ind/registration"
        self.expected_title = "WF: Investor Platform"

    def is_expected_title(self):
        """Verifies that the hardcoded text "WF: Investor Platform" appears in page title"""
        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(self.expected_title))
        finally:
            assert self.expected_title in self.driver.title
        waitForAngular(self.driver)


    def is_expected_landing_url(self):
        """Verifies that the hardcoded text "WF: Investor Platform" appears in page title"""
        try:
            wait = WebDriverWait(self.driver, 5).until(
                lambda wait: self.driver.current_url == self.expected_landing_url)
        finally:
            assert self.expected_landing_url in self.driver.current_url
        waitForAngular(self.driver)

    def enter_info(self, empStat, yes, no):
        assert self.employStatus is not None
        self.employStatus.send_keys(empStat)
        assert empStat in self.employStatus.get_attribute("value")

        assert self.otherOpportYes is not None
        self.otherOpportYes.send_keys(yes)
        assert yes in self.otherOpportYes.get_attribute("value")

        assert self.otherOpportNo is not None
        self.otherOpportNo.send_keys(no)
        assert no in self.otherOpportNo.get_attribute("value")


    def land(self):
        self.driver.get(self.expected_landing_url)


        def clickContinue(self):
            self.btnContinue.click()
            waitForAngular(self.driver)

        def clickEmployStatus(self):
            self.ddlInvestorEmploymentStatus.click()
            waitForAngular(self.driver)

        def clickOtherOpp(self):
            self.rbOtherOpportunitiesYes.click()
            waitForAngular(self.driver)

