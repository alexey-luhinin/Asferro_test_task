import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from utils.locators import GmailMailboxPageLocators
from utils.utils import create_random_string, count_digits, count_letters


class GmailMailboxPage(BasePage):
    def __init__(self, driver):
        self.locator = GmailMailboxPageLocators
        self._new_message_link = "https://mail.google.com/mail/u/0/#inbox?compose=new"
        self._to_addr = "testingqwerty11235@gmail.com"
        self._filter_link = "https://mail.google.com/mail/u/0/#advanced-search/is_unread=true&query=from%3A(testingqwerty11235%40gmail.com)+to%3A(testingqwerty11235%40gmail.com)&isrefinement=true"
        super(GmailMailboxPage, self).__init__(driver)

    def _send_letter(self, to, subject, text):
        self.open(self._new_message_link)
        to_addr = self.get_element_if_clickable(*self.locator.TO_ADDR)
        to_addr.send_keys(to)
        theme = self.get_element_if_clickable(*self.locator.SUBJECT)
        theme.send_keys(subject, Keys.TAB)
        body_text = self.driver.switch_to.active_element
        body_text.send_keys(text)
        body_text.send_keys(Keys.CONTROL, Keys.ENTER)

    def send_summary_letter(self, messages):
        self._send_letter(self._to_addr, "Summary", self._get_messages_info(messages))

    def filter_letters(self):
        time.sleep(2)
        self.open(self._filter_link)

    def send_letters(self, count=15):
        for _ in range(count):
            subject = create_random_string()
            text = create_random_string()
            self._send_letter(self._to_addr, subject, text)
            time.sleep(4)

    def get_letters(self):
        messages = {}
        for row in self.find_elements(*self.locator.EMAIL_LINK):
            message = row.text.split("\n")
            try:
                theme, _, text = message
            except ValueError:
                continue
            messages[theme.encode("utf8")] = text.encode("utf8")
        return messages

    def _get_messages_info(self, messages):
        full_message = ""
        for theme, text in messages.items():
            full_message += "Received mail on theme {} with message: {}. It contains {} letters and {} numbers\n".format(
                theme, text, count_letters(text), count_digits(text)
            )
        return full_message

    def remove_all_except_first(self):
        actions = ActionChains(self.driver)
        select_all = self.get_element_if_located(*self.locator.SELECT_ALL)
        actions.move_to_element(select_all).click()
        select_first = self.get_element_if_located(*self.locator.SELECT_FIRST)
        actions.move_to_element(select_first).click()
        delete_all = self.get_element_if_located(*self.locator.DELETE_ALL)
        actions.move_to_element(delete_all).click()
        actions.perform()
        time.sleep(2)

    def check_messages(self):
        messages = self.get_letters() or None
        return messages

    def remove_all(self):
        if not self.check_messages():
            return
        self.filter_letters()
        actions = ActionChains(self.driver)
        select_all = self.get_element_if_located(*self.locator.SELECT_ALL)
        actions.move_to_element(select_all).click()
        delete_all = self.get_element_if_located(*self.locator.DELETE_ALL)
        actions.move_to_element(delete_all).click()
        actions.perform()
        time.sleep(2)
