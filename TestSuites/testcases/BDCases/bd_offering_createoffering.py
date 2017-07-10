import unittest

from ..testpages.BDPages.bdofferingtab_page import BDOfferingTabPage
from ..testpages.BDPages.bdofferingtab_info import BDOfferingTabInfo
from ..testpages.BDPages.bdhomepage import BDHomePage
from ..testcaseutilities.testinfo import TestInfo


class TestBDOfferingCreateOffering(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_bd_offering_create_offering(self):

        BDHomePage().clickOfferingTab()



        offeringPage = BDOfferingTabPage()
        offeringPage.load_treenodes()

        # click on dots
        # assert offeringPage.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]] is not None
        offeringPage.treespace[self.lookup.testinfo['John ISS']][1].click()

        #click on create offering
        offeringPage.treespace[self.lookup.testinfo["John ISS"]][2][1].click()

        #====
        BDOfferingTabInfo().setDates()

        #===
        # bd_admintab_iss_page = BDAdminTabIssPage()
        # bd_admintab_iss_page.fill_elements(self.lookup.testinfo["testissinfo"])
        #
        # bd_admintab_iss_page.submit()
        #
        # offeringPage.load_treenodes()
        #
        # offeringPage.get_treenode([self.lookup.testinfo["testissinfo"]["displayNameInput"]]).click()
        #
        # bd_admintab_iss_page.verify_elements(self.lookup.testinfo["testissinfo"])

        # while True:
        #     pass

        # bd_admintab_user_page = BDAdminTabUserPage(self.driver)
        # bd_admintab_user_page.enter_info(self.lookup.testinfo["NewBDUser.First Name"], self.lookup.testinfo["NewBDUser.Last Name"], self.lookup.testinfo["NewBDUser.Email"])
        # bd_admintab_user_page.add_role(self.lookup.testinfo["NewBDUser.Role1"])
        # bd_admintab_user_page.submit()
        #
        #
        # bd_admintab_page.load_treenodes()
        #
        # #click on newly created user's tree node
        # bd_admintab_page.treespace[self.lookup.testinfo["NewBDUser.Full Name"]].click()
        #
        # bd_admintab_user_page.first_name_should_be(self.lookup.testinfo["NewBDUser.First Name"])
        # bd_admintab_user_page.last_name_should_be(self.lookup.testinfo["NewBDUser.Last Name"])
        # bd_admintab_user_page.email_should_be(self.lookup.testinfo["NewBDUser.Email"])
        # bd_admintab_user_page.roles_should_contain(self.lookup.testinfo["NewBDUser.Role1"])
        #
        # # print(get_new_bd_user_password_reset_url(self.lookup.testinfo["environment"]))
        # bdconfirmuser_page = BDConfirmUserPage(self.driver, get_new_bd_user_password_reset_url(self.lookup.testinfo["environment"], self.lookup.testinfo["NewBDUser.Email"]))
        # bdconfirmuser_page.land()
        # bdconfirmuser_page.enter_password(self.lookup.testinfo["NewBDUser.Password"])
        # bdconfirmuser_page.submit()
        #
        # bdconfirmuser_success_page = BDConfirmUserSuccessPage(self.driver)
        # bdconfirmuser_success_page.submit()
        #
        # bd_login_page.login(self.lookup.testinfo["NewBDUser.Email"],self.lookup.testinfo["NewBDUser.Password"])


        # while True:
        #     pass



    # def tearDown(self):
    #     self.driver.close()



if __name__ == "__main__":
    unittest.main()
