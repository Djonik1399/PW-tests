import random
from Locators.personal import Personal
from pages.base import Base
from data.assertions import Assertions
from playwright.sync_api import Page
import asyncio


class PersonalPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def checkout_titles(self):
        self.assertion.contain_text(Personal.FOR_AUTHOR, "Об авторе", "Not found title for personalPage For Author")
        self.assertion.contain_text(Personal.BLOG, "Блог", "Not found title for personalPage Blog")

    def checkout_button(self):
        self.assertion.check_presence(Personal.SUPPORT_BTN, "Not found button track")

    def go_to_blog_and_add_comment(self):

        self.click(Personal.BLOG)
        comment_on_blog = f"Комментарий под последним блогом {str(random.randint(1, 1000))}"
        self.input_value_by_index(Personal.AREA_FOR_COMMENT,0, comment_on_blog)
        self.click_first_element(Personal.COMMENT_BTN)

        last_comment = self.get_text_element_by_index_all_elements(Personal.LAST_POST, Personal.COMMENT_TEXT, -1).inner_text()
        self.refresh()
        self.assertion.check_equals(comment_on_blog, last_comment, "Comments don't equals")


    def click_support_and_check(self):
        self.click(Personal.SUPPORT_BTN)
        self.assertion.check_URL("user/42/support", "Wrong URL")

    def click_track_and_check_style(self):
        btn_title = self.page.locator(Personal.TRACK_BTN).get_attribute("title")
        if btn_title == 'Удалить из закладок':
            self.click(Personal.TRACK_BTN)

        element = self.page.query_selector(Personal.TRACK_BTN)
        original_style_button = element.evaluate("el => window.getComputedStyle(el).color", element)
        self.click(Personal.TRACK_BTN)

        style_button_after_click = element.evaluate("el => window.getComputedStyle(el).color", element)
        self.assertion.check_not_equal(original_style_button, style_button_after_click, "Style of button don't changed")

        self.click(Personal.FAVORITES_PROJECTS)

    def go_to_favorites(self):
        self.click(Personal.FAVORITES_PROJECTS)