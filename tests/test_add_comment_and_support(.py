import pytest
from pages.main_page import MainPage
from pages.personal_page import PersonalPage

@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestAddComment:
    def test_add_comment_and_support(self, browser):
        mainPage = MainPage(browser)
        mainPage.check_count_projects()
        mainPage.click_popular_card_check()
        personalPage = PersonalPage(browser)
        personalPage.checkout_titles()
        personalPage.checkout_button()
        personalPage.go_to_blog_and_add_comment()
        personalPage.click_support_and_check()
