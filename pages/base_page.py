from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 25

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, url):
        self.driver.get(url)

    def get_element_if_located(self, *locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print("Can't find element by locator {}".format(locator[1]))
            self.driver.quit()

    def get_element_if_clickable(self, *locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            print("Can't find element by locator {}".format(locator[1]))
            self.driver.quit()
