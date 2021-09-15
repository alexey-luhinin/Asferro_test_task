import pytest
from selenium import webdriver


class BaseTest(object):
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)

    def teardown_class(self):
        self.driver.close()
