from tests.base_test import BaseTest
from pages.gmail_main_page import GmailMainPage
from pages.gmail_login_page import GmailLoginPage
from pages.gmail_mailbox_page import GmailMailboxPage



class TestGmailMainPage(BaseTest):
    def test_page_load(self):
        self.page = GmailMainPage(self.driver)
        assert self.page.check_page_loaded()

    def test_click_sign_in(self):
        self.page = GmailMainPage(self.driver)
        assert self.page.click_sign_in()

    def test_login(self):
        self.page = GmailLoginPage(self.driver)
        self.page.check_login()

    def test_sended_messages(self):
        self.page = GmailMailboxPage(self.driver)
        self.page.remove_all()
        self.page.send_letters()
        messages = self.page.get_letters()
        self.page.send_summary_letter(messages)
        self.page.filter_letters()
        self.page.remove_all_except_first()
        assert len(messages) == 15
