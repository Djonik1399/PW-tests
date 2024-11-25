from Locators.favorites import Favorites
from pages.base import Base
from data.assertions import Assertions
from playwright.sync_api import Page

class FavoritePage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def checkout_on_favorite_page(self):
        self.assertion.check_URL("user/336/favorite-creators", "Wrong URL")
        self.assertion.contain_text(Favorites.FAVORITES_TITLE, "Мои избранные проекты", "Expected title about NOT empty favorites projects")
        self.assertion.check_presence(Favorites.FAVORITES_PROJECTS,"Expected NOT empty favorites projects")

    def delete_favorites_cards_and_check(self):
        self.click(Favorites.DELETE_FAVORITES_BTN)

        self.refresh()

        self.assertion.contain_text(Favorites.FAVORITES_TITLE, "В настоящий момент у вас нет избранных проектов","Expected title about empty favorites projects")
        self.assertion.check_absence(Favorites.FAVORITES_PROJECTS, "Expected empty favorites projects")



