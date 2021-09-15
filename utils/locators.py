from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SIGN_IN = (By.XPATH, "/html/body/header/div/div/div/a[2]")


class GmailLoginPageLocators(object):
    EMAIL_INPUT = (By.XPATH, "//*[@id='identifierId']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")
    CONTINUE_BUTTON_LOGIN = (By.XPATH, "//*[@id='identifierNext']/div/button")
    CONTINUE_BUTTON_PASSWORD = (By.XPATH, "//*[@id='passwordNext']/div/button")
    SEARCH_INPUT = (By.XPATH, "//*[@id='gs_lc50']/input[1]")


class GmailMailboxPageLocators(object):
    TO_ADDR = (By.NAME, "to")
    SUBJECT = (By.NAME, "subjectbox")
    EMAIL_LINK = (By.CSS_SELECTOR, "div[role='link']")
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
