from pages.base import Base
from data.constants import Constants
from Locators.auth import Auth
from Locators.main import Main
from data.assertions import Assertions
from playwright.sync_api import Page


class MainPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open("")
        self.click(Main.SIGN_UP)
        self.input(Auth.USEREMAIL_INPUT, Constants.email)
        self.input(Auth.PASSWORD_INPUT, Constants.password)
        self.click(Auth.LOGIN_BTN)
        self.assertion.check_URL("", "Wrong URL")

    def click_popular_card_check(self):
        self.click_first_element(Main.CARDS_OF_POPULAR)

    def check_count_projects(self):
        self.assertion.count_elements(Main.CARDS_OF_POPULAR, 6, "Not found 6 popular cards")
