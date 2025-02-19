from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

from data.locators import CategoryPageLocators
import time


class  CategoryPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://club-administration.qa.qubika.com/"
        self.locator = CategoryPageLocators
        super().__init__(driver, wait)

    def open_category_option(self):
        category_menu = self.wait.until(EC.element_to_be_clickable(self.locator.CATEGORY_MENU_OPTION))
        category_menu.click()
        self.wait.until(EC.presence_of_all_elements_located(self.locator.CATEGORY_TABLE_TITLE))
        self.driver.save_screenshot("results/results-category.png")

    def create_category(self, category_name):
        add_button = self.wait.until(EC.element_to_be_clickable(self.locator.ADD_BUTTON))
        add_button.click()

        name_input = self.wait.until(EC.visibility_of_element_located(self.locator.CATEGORY_NAME_INPUT))
        name_input.clear()
        name_input.send_keys(category_name)

        save_button = self.wait.until(EC.element_to_be_clickable(self.locator.SAVE_BUTTON))
        save_button.click()

        self.wait.until(EC.presence_of_all_elements_located(self.locator.CATEGORY_TABLE_TITLE))
        time.sleep(2)

    def create_sub_category(self, parent_category,sub_category_name):
        add_button = self.wait.until(EC.element_to_be_clickable(self.locator.ADD_BUTTON))
        add_button.click()

        name_input = self.wait.until(EC.visibility_of_element_located(self.locator.CATEGORY_NAME_INPUT))
        name_input.clear()
        name_input.send_keys(sub_category_name)

        is_sub_category_input_div = self.wait.until(EC.element_to_be_clickable(self.locator.IS_SUBCATEGORY_CHECKBOX_DIV))
        is_sub_category_input_div.click()

        sub_category_selector_input = self.wait.until(EC.visibility_of_element_located(self.locator.SUB_CATEGORY_INPUT))
        sub_category_selector_input.send_keys(parent_category)
        sub_category_selector_input.send_keys(Keys.RETURN)
        sub_category_selector_input.click()

        sub_category_selector_item = self.wait.until(EC.element_to_be_clickable(self.locator.SUB_CATEGORY_ITEM))
        sub_category_selector_item.click()

        save_button = self.wait.until(EC.element_to_be_clickable(self.locator.SAVE_BUTTON))
        save_button.click()

        self.wait.until(EC.presence_of_all_elements_located(self.locator.CATEGORY_TABLE_TITLE))
        time.sleep(2)
