import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.coreLoginPage import coreLoginPage

"""from Driver.DriverFixture import driver"""
from Pages.BasePage import BasePage
from Pages.LoginPage import login_Page


class ManageEmailTemplates(BasePage):
    manage_email_templates_menu_link = (By.XPATH, "//div[contains(text(),'Manage Email Templates')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.IQA_Success_URL)
        # self.loginPage = login_Page(self.driver)
        self.coreLoginPage = coreLoginPage(self.driver)

    def do_click_manage_email_templates_users(self):

        self.coreLoginPage.do_coreLogin(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(2)
        self.do_click(self.coreLoginPage.app_launcher)
        time.sleep(2)
        self.do_click(self.coreLoginPage.select_admin_app)
        time.sleep(2)
        # self.do_click(self.coreLoginPage.select_admin_app_xpath)
        self.do_click(self.coreLoginPage.user_side_navi)
        self.do_click(self.manage_email_templates_menu_link)
        time.sleep(5)
