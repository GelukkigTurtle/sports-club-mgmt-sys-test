from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
    DASHBOARD_RESULTS = (By.XPATH, "//*[app-admin-layout]")
