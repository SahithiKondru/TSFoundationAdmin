from selenium.webdriver.common.by import By

from Config.config import TestData

"""from Driver.DriverFixture import driver"""
from Pages.BasePage import BasePage
from Pages.LoginPage import login_Page


class exportUsersPage(BasePage):
    "By locators or Object Repository"
    home_side_navi = (By.XPATH, "//span[@class='nav-side-control']")
    manage_users_side_navi = (By.XPATH, "//div[contains(text(),'Manage Users')]")
    export_users_link = (By.XPATH, "//div[contains(text(),'Export users')]")
    export_users_header = (By.XPATH, "//h1[normalize-space()='Export Users']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_export_users_title(self, title):
        return self.get_title(title)

    def get_export_users_header(self):
        if self.is_visible(self.export_users_header):
            return self.get_element_text(self.export_users_header)

    def do_click_export_users(self):
        self.do_click(self.home_side_navi)
        self.do_click(self.manage_users_side_navi)
        self.do_click(self.export_users_link)

    def do_click_export_users_withoutmanageusers(self):
        self.do_click(self.home_side_navi)
        self.do_click(self.export_users_link)

    def select_export_users(self):
        self.do_click(self.export_users_link)