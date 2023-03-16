from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

""""This Class is the parent of all pages. It contains all generic methods and utilities for all the pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    # def screenShot(self, resultMessage):
    #     """
    #     Takes screenshot of the page and save in .png format
    #     """
    #     fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
    #     screenshotDirectory = "../screenshots/"
    #     relativeFileName = screenshotDirectory + fileName
    #     currentDirectory = os.path.dirname(__file__)
    #     destinationFile = os.path.join(currentDirectory, relativeFileName)
    #     destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
    #
    #     try:
    #         if not os.path.exists(destinationDirectory):
    #             os.makedirs(destinationDirectory)
    #         self.driver.save_screenshot(destinationFile)
    #         self.log.info("Screenshot save to directory: " + destinationFile)
    #     except:
    #         self.log.error("### Exception Occurred while taking screenshot")