import unittest

from ..testpages.BDPages.bdloginpage import BDLoginPage
from ..testpages.BDPages.bdadmintab_page import BDAdminTabPage
from ..testpages.BDPages.bdadmintab_user_page import BDAdminTabUserPage
from ..testpages.BDPages.bdconfirmuser_page import BDConfirmUserPage
from ..testpages.BDPages.bdconfirmuser_success_page import BDConfirmUserSuccessPage
from ..testcaseutilities.gmailaccessor import get_new_bd_user_password_reset_url
from ..testcaseutilities.testinfo import TestInfo


class TestBDInviteUser(unittest.TestCase):

    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_bd_invite_cco(self):
        bd_admintab_page = BDAdminTabPage()
        bd_admintab_page.is_expected_landing_url()
        bd_admintab_page.load_treenodes()

        # click on dots
        assert bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]] is not None
        bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]][1].click()

        #click on create user under WealthForgeSecurities BD
        bd_admintab_page.treespace[self.lookup.testinfo["BD.WealthForge Securities.Display Name"]][2][2].click()

        bd_admintab_user_page = BDAdminTabUserPage()
        bd_admintab_user_page.enter_info(self.lookup.testinfo["NewBDUser.First Name"], self.lookup.testinfo["NewBDUser.Last Name"], self.lookup.testinfo["NewBDUser.Email"])
        bd_admintab_user_page.add_role(self.lookup.testinfo["NewBDUser.Role1"])
        bd_admintab_user_page.submit()


        bd_admintab_page.load_treenodes()

        #click on newly created user's tree node
        bd_admintab_page.treespace[self.lookup.testinfo["NewBDUser.Full Name"]].click()

        bd_admintab_user_page.first_name_should_be(self.lookup.testinfo["NewBDUser.First Name"])
        bd_admintab_user_page.last_name_should_be(self.lookup.testinfo["NewBDUser.Last Name"])
        bd_admintab_user_page.email_should_be(self.lookup.testinfo["NewBDUser.Email"])
        bd_admintab_user_page.roles_should_contain(self.lookup.testinfo["NewBDUser.Role1"])

        # print(get_new_bd_user_password_reset_url(self.lookup.testinfo["environment"]))
        bdconfirmuser_page = BDConfirmUserPage(get_new_bd_user_password_reset_url(self.lookup.testinfo["environment"], self.lookup.testinfo["NewBDUser.Email"]))
        bdconfirmuser_page.land()
        bdconfirmuser_page.enter_password(self.lookup.testinfo["NewBDUser.Password"])
        bdconfirmuser_page.submit()

        bdconfirmuser_success_page = BDConfirmUserSuccessPage()
        bdconfirmuser_success_page.submit()

        bd_login_page = BDLoginPage()

        bd_login_page.login(self.lookup.testinfo["NewBDUser.Email"], self.lookup.testinfo["NewBDUser.Password"])


        while True:
            pass



if __name__ == "__main__":
    unittest.main()
