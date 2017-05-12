from selenium.webdriver.support.ui import WebDriverWait
from .element import PageElement
from .basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .testpageutilities.waitforangular import waitForAngular
import time


class BDAdminTabUserPage(BasePage):
    # https://qa1.wealthforge.org/BD/#/rad
    firstName = PageElement(id_='fnameInput')
    lastName = PageElement(id_='lnameInput')
    email = PageElement(id_='emailInput')
    # TODO: add hooks to current role list
    rolesDropdown = PageElement(id_='RoleSelect')
    rolesAdd = PageElement(xpath="//button[contains(@ng-click,'addRole')]")
    submitButton = PageElement(xpath="//button[contains(@ng-click,'submit()')]")
    rolesRepeater = PageElement(xpath="//li[contains(@ng-repeat,'roles')]")

    # TODO: roles submit
    # TODO: save button

    def __init__(self, driver):
        self.driver = driver
        self.expected_title = "WF: Broker Dealer"
        roles_repeater = []

    def is_expected_title(self):
        try:
            wait = WebDriverWait(self.driver, 5).until(
                EC.title_contains(self.expected_title))
        finally:
            assert self.expected_title in self.driver.title
        waitForAngular(self.driver)

    # def is_expected_landing_url(self):
    #     """Verifies that the hardcoded text "WF: Login" appears in page title"""
    #     assert self.expected_landing_url in self.driver.current_url

    # def land(self):
    #     self.driver.get(self.expected_landing_url)

    #20170508 - A CCO can create:
    #Chief Compliance Officer
    #General Securities Principle
    #Compliance Analyst
    #Fingerprinted Person
    #Financial Analyst
    def add_role(self, role):
        assert self.rolesDropdown is not None
        Select(self.rolesDropdown).select_by_visible_text(role)
        self.rolesAdd.click()
        waitForAngular(self.driver)



    def enter_info(self, first, last, email):
        assert self.firstName is not None
        self.firstName.send_keys(first)
        assert first in self.firstName.get_attribute("value")

        assert self.lastName is not None
        self.lastName.send_keys(last)
        assert last in self.lastName.get_attribute("value")

        assert self.email is not None
        self.email.send_keys(email)
        assert email in self.email.get_attribute("value")


    def submit(self):
        assert self.submitButton is not None
        self.submitButton.click()
        waitForAngular(self.driver)


    def first_name_should_be(self, expected_firstname):
        waitForAngular(self.driver)
        assert self.firstName is not None
        assert expected_firstname in self.firstName.get_attribute("value")

    def last_name_should_be(self, expected_lastname):
        waitForAngular(self.driver)
        assert self.lastName is not None
        assert expected_lastname in self.lastName.get_attribute("value")

    def email_should_be(self, expected_email):
        waitForAngular(self.driver)
        assert self.email is not None
        assert expected_email in self.email.get_attribute("value")


    def roles_should_contain(self, role):
        waitForAngular(self.driver)
        assert self.driver.find_elements_by_xpath("//li[contains(@ng-repeat,'roles')]") is not None
        for eachrole in self.driver.find_elements_by_xpath("//li[contains(@ng-repeat,'roles')]"):
            if role in eachrole.get_attribute("textContent"):
                assert True
                return
        assert False






        # TODO: test current role list
