import os

import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = LoginPage(self.driver, self.wait)
        self.page.open_login_page()

    def test_title(self, load_pages):
        self.page.check_title("Qubika Club")

    def test_login(self, load_pages):
        self.page.do_login(os.environ["TEST_USERNAME"],os.environ["TEST_PASSWORD"])