import pytest
import time

from Config.config import TestData
from Pages.LoginPage import login_Page
from Tests.test_Base_Login import BaseTest
from Pages.adminManageEmailTemplates import ManageEmailTemplates


class Tests_ManageEmailTemplates(BaseTest):

    def test_testManageEmailTemplates(self):

        self.ManageEmailTemplates = ManageEmailTemplates(self.driver)

        self.ManageEmailTemplates.do_click_manage_email_templates_users()
        # iuheader = self.importUserPage.get_import_users_header()
        # assert iuheader == "Import Users"
        # time.sleep(5)
        # self.exportUserPage.do_click_export_users_withoutmanageusers()
        # euheader = self.exportUserPage.get_export_users_header()
        # assert euheader == "Export Users"
        # time.sleep(3)
        # self.loginPage.do_logout()
        # print("ADMIN_LOGOUT IS SUCCESSFUL")
