import pytest
from pages.main_page import MainPage

@pytest.fixture(scope='class')
def user_login(browser):
    m = MainPage(browser)
    m.user_login()