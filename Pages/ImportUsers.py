from selenium.webdriver.common.by import By

from Config.config import TestData

"""from Driver.DriverFixture import driver"""
from Pages.BasePage import BasePage
from Pages.LoginPage import login_Page


class ImportUsersPage(BasePage):
    "By locators or Object Repository"
    home_side_navi = (By.XPATH, "//span[@class='nav-side-control']")
    manage_users_side_navi = (By.XPATH, "//div[contains(text(),'Manage Users')]")
    import_users_link = (By.XPATH, "//div[contains(text(),'Import users')]")
    import_users_header = (By.XPATH, "//h1[normalize-space()='Import Users']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_import_users_title(self, title):
        return self.get_title(title)

    def get_import_users_header(self):
        if self.is_visible(self.import_users_header):
            return self.get_element_text(self.import_users_header)

    def do_click_import_users(self):
        self.do_click(self.home_side_navi)
        self.do_click(self.manage_users_side_navi)
        self.do_click(self.import_users_link)
        # mo = self.get_title(self.import_users_title)
        # assert mo == "Import Users"
