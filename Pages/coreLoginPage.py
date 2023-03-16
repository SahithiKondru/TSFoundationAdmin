import time

from selenium.webdriver.common.by import By

from Config.config import TestData

"""from Driver.DriverFixture import driver"""
from Pages.BasePage import BasePage


class coreLoginPage(BasePage):

    """By locators or Object Repository"""
    login_user_name = (By.NAME, "userName")
    login_password = (By.NAME, 'password')
    login_button = (By. NAME, 'loginBtn')
    login_title = (By.XPATH, "//span[@id='navTitle']")
    app_launcher = (By.CSS_SELECTOR, ".app-launcher-icon")
    select_admin_app = (By.CSS_SELECTOR, ".app-icon.app-icon-TSADMIN.app-icon-selected")
    # select_admin_app_xpath = (By.XPATH, "//span[@class='app-icon app-icon-TSADMIN app-icon-selected']")
    account_user_menu = (By.XPATH, "//span[@class='user-menu-icon']")
    user_logout = (By.XPATH, "//li[normalize-space()='Log Out']")
    home_screen =(By.XPATH,"//span[@id='navTitle']")
    user_side_navi = (By.XPATH,"//span[@class='nav-side-control']")
    security_link = (By.LINK_TEXT,"Security")
    # security_settings = (By.XPATH, "//div[contains(text(),'Security Settings')]")
    security_settings = (By.LINK_TEXT, "Security Settings")
    pages = (By.LINK_TEXT,"Pages")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.CORE_BASE_URL)


    """this is used to login to  CORE application"""

    def do_coreLogin(self, username, password):
        self.do_send_keys(self.login_user_name, username)
        self.do_send_keys(self.login_password, password)
        self.do_click(self.login_button)
        time.sleep(5)

    """ this is used to logout from application"""

    def do_coreLogout(self):
        time.sleep(3)
        self.do_click(self.account_user_menu)
        time.sleep(3)
        self.do_click(self.user_logout)
        time.sleep(3)
        print("CoreLogout Successful")

    def do_click_security_settings(self):
        self.do_click(self.user_side_navi)
        self.do_click(self.pages)
        time.sleep(5)
        self.do_click(self.security_settings)
        time.sleep(3)


