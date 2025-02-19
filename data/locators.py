from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@type='submit']")
    DASHBOARD_RESULTS = (By.XPATH, "//*[app-admin-layout]")
class CategoryPageLocators:
    CATEGORY_MENU_OPTION = (By.CSS_SELECTOR, "a[href='#/category-type']")
    CATEGORY_TABLE_TITLE = (By.XPATH, "//app-table-generic//h3")
    ADD_BUTTON = (By.XPATH, "//app-table-generic//button[contains(@class, 'btn-primary')]")
    CATEGORY_NAME_INPUT = (By.ID,"input-username")
    IS_SUBCATEGORY_CHECKBOX_DIV = (By.XPATH, "//app-tables/form//label/span")
    IS_SUBCATEGORY_CHECKBOX = (By.ID, "customCheckMain")
    SUB_CATEGORY_INPUT = (By.XPATH, "//app-tables/form//ng-select//input")
    SUB_CATEGORY_ITEM = (By.XPATH, "//ng-dropdown-panel//div[contains(@class, 'ng-option')][1]/span")
    SAVE_BUTTON = (By.XPATH, "//app-tables/form//button[contains(@class, 'btn-primary')]")
