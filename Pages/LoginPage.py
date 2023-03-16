import time

from selenium.webdriver.common.by import By

from Config.config import TestData

"""from Driver.DriverFixture import driver"""
from Pages.BasePage import BasePage


class login_Page(BasePage):

    "By locators or Object Repository"
    login_user_name = (By.ID, "userName")
    login_password = (By.ID, 'password')
    login_button = (By. ID, 'loginBtn')
    login_title = (By.XPATH, "//span[@id='navTitle']")
    account_user_menu = (By.XPATH, "//span[@class='user-menu-icon']")
    user_logout = (By.XPATH, "//li[normalize-space()='Log Out']")
    home_screen =(By.XPATH,"//span[@id='navTitle']")
    user_side_navi = (By.XPATH,"//span[@class='nav-side-control']")
    security_settings = (By.LINK_TEXT,"Security")
    forgot_password = (By.ID, 'forgotPwd')

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        time.sleep(3)

    """Page Actions for Login page"""
    """This method is used to get page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this method is used to login to application"""
    def do_login(self, username, password):
        self.do_send_keys(self.login_user_name, username)
        self.do_send_keys(self.login_password, password)
        self.do_click(self.login_button)

    """ this method is used to logout from application"""
    def do_logout(self):
        time.sleep(3)
        self.do_click(self.account_user_menu)
        time.sleep(5)
        self.do_click(self.user_logout)
        time.sleep(5)
        print("Logout Successful")