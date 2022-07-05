from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from GeneralPackage import GeneralInformation
from Locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging


ga_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
wait = WebDriverWait(ga_driver, 10)


class GeneralActions:
    driver = ga_driver
    logging.basicConfig(filename='TestRun.log', encoding='utf-8', level=logging.INFO, filemode='a',
                        format='%(asctime)s :: %(funcName)s :: %(levelname)s :: %(message)s')

    add_log = logging

    # COMMON ACTIONS
    def open_and_maximize_window(self):
        self.driver.get(LoginPageLocators.HOME_URL)
        self.driver.maximize_window()

    def correct_login(self):
        # NAVIGATE TO LOGIN PAGE
        print("Login with valid credentials")

        # ENTER VALID USERNAME
        wait.until(ec.presence_of_element_located((By.XPATH, LoginPageLocators.USERNAME_FIELD)))
        self.locate_and_send_keys(LoginPageLocators.USERNAME_FIELD, GeneralInformation.VALID_USERNAME)
        # ENTER VALID PASSWORD
        self.locate_and_send_keys(LoginPageLocators.PASSWORD_FIELD, GeneralInformation.VALID_PASSWORD)
        # CLICK LOGIN BUTTON
        self.locate_and_click(LoginPageLocators.LOGIN_BUTTON)

    def locate_with_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def locate_and_send_keys(self, xpath, text_to_send):
        self.locate_with_xpath(xpath).send_keys(text_to_send)

    def locate_and_click(self, xpath):
        self.locate_with_xpath(xpath).click()

    def locate_and_assert_text(self, xpath, text_to_verify_present):
        element_text = self.locate_with_xpath(xpath).text
        assert text_to_verify_present in element_text

