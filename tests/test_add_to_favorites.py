import pytest
from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from pages.favorite_page import FavoritePage

@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestAddToFavorites:
    def test_add_to_favorites(self, browser):
        mainPage = MainPage(browser)
        mainPage.click_popular_card_check()
        personalPage = PersonalPage(browser)
        personalPage.click_track_and_check_style()
        personalPage.go_to_favorites()
        favoritePage = FavoritePage(browser)
        favoritePage.checkout_on_favorite_page()
        favoritePage.delete_favorites_cards_and_check()

