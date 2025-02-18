from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://club-administration.qa.qubika.com/"
        self.locator = LoginPageLocators
        super().__init__(driver, wait)

    def open_login_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        self.wait.until(EC.title_contains(title))

    def do_login(self, username,password):
        email_input = self.wait.until(EC.visibility_of_element_located(self.locator.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(username)

        password_input = self.wait.until(EC.visibility_of_element_located(self.locator.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable(self.locator.LOGIN_BUTTON))
        login_button.click()

        self.wait.until(EC.presence_of_all_elements_located(self.locator.DASHBOARD_RESULTS))
        self.driver.save_screenshot("results/results.png")
