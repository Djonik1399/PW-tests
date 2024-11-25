from pages.base import Base
from Locators.overview import Overview
from Locators.search import Search
from Locators.main import Main
from data.assertions import Assertions
from playwright.sync_api import Page

class OverviewPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def fill_data_and_goto_results(self):
        self.click(Main.OVERVIEW)
        self.input(Overview.SEARCH_INPUT, "Привет")
        self.click(Overview.SEARCH_BUTTON)

    def check_results_searching(self):
        total_projects = self.get_text(Search.SEARCH_RESULTS_PROJECTS, 0).strip()
        total_posts = self.get_text(Search.SEARCH_RESULTS_POST, 0).strip()
        self.assertions.check_equals(total_projects, "Проекты (1)", "Incorrect result project search text")
        self.assertions.check_equals(total_posts, "Посты (1)", "Incorrect result posts search text")

    def click_project_card(self):
        self.click(Search.CARDS_OF_SEARCHING)
        self.assertions.check_URL("svetlana", "Wrong URL")

