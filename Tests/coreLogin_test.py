import time

import pytest
from Config.config import TestData
from Pages.coreLoginPage import coreLoginPage
from Tests.test_Base_Login import BaseTest


class Tests_coreLoginTest(BaseTest):

    @pytest.mark.login
    def test_corelogin(self):
        self.coreLoginPage = coreLoginPage(self.driver)
        self.coreLoginPage.do_coreLogin(TestData.USER_NAME, TestData.PASSWORD)
        #self.coreLoginPage.do_click_app_launcher()
        time.sleep(2)
        self.coreLoginPage.do_coreLogout()
        time.sleep(5)
        print("CORE_LOGOUT IS SUCCESSFUL")
