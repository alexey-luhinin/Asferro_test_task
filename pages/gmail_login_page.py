from pages.base_page import BasePage
from utils.locators import GmailLoginPageLocators
import time


class GmailLoginPage(BasePage):
    def __init__(self, driver):
        self.locator = GmailLoginPageLocators
        self._login = "testingqwerty11235@gmail.com"
        self._password = "qwerty11235"
        super(GmailLoginPage, self).__init__(driver)

    def check_login(self):
        self.get_element_if_clickable(*self.locator.EMAIL_INPUT)
        email_input = self.find_element(*self.locator.EMAIL_INPUT)
        email_input.send_keys(self._login)
        self.get_element_if_clickable(*self.locator.CONTINUE_BUTTON_LOGIN)
        continue_button_login = self.find_element(*self.locator.CONTINUE_BUTTON_LOGIN)
        continue_button_login.click()
        self.get_element_if_clickable(*self.locator.PASSWORD_INPUT)
        password_input = self.find_element(*self.locator.PASSWORD_INPUT)
        password_input.send_keys(self._password)
        self.get_element_if_clickable(*self.locator.CONTINUE_BUTTON_PASSWORD)
        continue_button_password = self.find_element(
            *self.locator.CONTINUE_BUTTON_PASSWORD
        )
        continue_button_password.click()

        assert self.get_element_if_located(*self.locator.SEARCH_INPUT)
