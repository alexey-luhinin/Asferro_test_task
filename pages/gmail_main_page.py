from pages.base_page import BasePage
from utils.locators import MainPageLocators


class GmailMainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super(GmailMainPage, self).__init__(driver)

    def check_page_loaded(self):
        self.open("https://www.google.com/intl/en/gmail/about/")
        return True if self.find_element(*self.locator.SIGN_IN) else False

    def click_sign_in(self):
        try:
            self.get_element_if_clickable(*self.locator.SIGN_IN).click()
            return True
        except:
            return False
