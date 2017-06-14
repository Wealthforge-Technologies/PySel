import unittest

from ..testpages.BDPages.bdadmintab_iss_page import BDAdminTabIssPage
from ..testpages.BDPages.bdadmintab_page import BDAdminTabPage

from ..testcaseutilities.testinfo import TestInfo


class TestBDAdminCreateIssuer(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_bd_admin_create_issuer(self):
        # bd_login_page = BDLoginPage()
        #
        #
        # bd_login_page.land()
        # bd_login_page.is_expected_landing_url()
        # bd_login_page.login(self.lookup.testinfo["CCO.email"],self.lookup.testinfo["CCO.password"])
        #
        # bd_home_page = BDHomePage()
        # bd_home_page.is_expected_landing_url()
        # bd_home_page.menuDashboardAdmin.click()
        #
        bd_admintab_page = BDAdminTabPage()
        # bd_admintab_page.is_expected_landing_url()
        bd_admintab_page.load_treenodes()

        # click on dots
        assert bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]] is not None
        bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]][1].click()

        #click on create iss under WealthForgeSecurities BD
        bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]][2][1].click()

        bd_admintab_iss_page = BDAdminTabIssPage()
        bd_admintab_iss_page.fill_elements(self.lookup.testinfo["testissinfo"])

        bd_admintab_iss_page.submit()

        bd_admintab_page.load_treenodes()

        bd_admintab_page.get_treenode([self.lookup.testinfo["testissinfo"]["displayNameInput"]]).click()

        bd_admintab_iss_page.verify_elements(self.lookup.testinfo["testissinfo"])

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
