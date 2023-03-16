import pytest
import time

from Config.config import TestData
from Pages.LoginPage import login_Page
from Tests.test_Base_Login import BaseTest
from Pages.ImportUsers import ImportUsersPage
from Pages.exportUsers import exportUsersPage


class Tests_Login(BaseTest):
    @pytest.mark.login
    def test_login(self):
        self.loginPage = login_Page(self.driver)
        self.importUserPage = ImportUsersPage(self.driver)
        self.exportUserPage = exportUsersPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.importUserPage.do_click_import_users()
        iuheader = self.importUserPage.get_import_users_header()
        assert iuheader == "Import Users"
        time.sleep(5)
        self.exportUserPage.do_click_export_users_withoutmanageusers()
        euheader = self.exportUserPage.get_export_users_header()
        assert euheader == "Export Users"
        time.sleep(3)
        self.loginPage.do_logout()
        print("ADMIN_LOGOUT IS SUCCESSFUL")
