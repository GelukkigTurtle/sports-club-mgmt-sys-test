import os

import pytest
from pages.category_page import CategoryPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from faker import Faker


class TestCategory(BaseTest):

    @pytest.fixture
    def login(self):
        login_page = LoginPage(self.driver, self.wait)
        login_page.open_login_page()
        login_page.do_login(os.environ["TEST_USERNAME"], os.environ["TEST_PASSWORD"])
    @pytest.fixture
    def go_to_categories(self, login):
        self.category_page = CategoryPage(self.driver, self.wait)
        self.category_page.open_category_option()
        self.fake = Faker()
        return self.category_page

    @pytest.fixture
    def new_category(self, go_to_categories):
        category_name = "AUTO-CAT-" + self.fake.name()
        self.category_page.create_category(category_name)
        return category_name

    def test_new_category(self, go_to_categories):
        category_name = "AUTO-CAT-" + self.fake.name()
        self.category_page.create_category(category_name)
        return category_name

    def test_new_sub_category(self, login, new_category):
        category_name = new_category
        self.category_page.create_sub_category(category_name, "AUTO-SUB-CAT-" + self.fake.name())
