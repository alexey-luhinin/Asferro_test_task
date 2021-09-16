from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SIGN_IN = (By.XPATH, "//a[@data-action='sign in']")


class GmailLoginPageLocators(object):
    EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    CONTINUE_BUTTON_LOGIN = (By.XPATH, "//*[@id='identifierNext']/div/button")
    CONTINUE_BUTTON_PASSWORD = (By.XPATH, "//*[@id='passwordNext']/div/button")
    SEARCH_INPUT = (By.XPATH, "//input[@name='q']")


class GmailMailboxPageLocators(object):
    TO_ADDR = (By.XPATH, "//textarea[@name='to']")
    SUBJECT = (By.XPATH, "//input[@name='subjectbox']")
    EMAIL_LINK = (By.XPATH, "//div[@role='link']")
    SELECT_ALL = (
        By.XPATH,
        "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/span",
    )

    SELECT_FIRST = (
        By.XPATH,
        "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[2]/div/table/tbody/tr[1]/td[2]/div",
    )

    DELETE_ALL = (
        By.XPATH,
        "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div",
    )
