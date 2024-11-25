import allure
from playwright.sync_api import Page
from data.environment import host
from playwright.sync_api import expect
from pages.base import Base

class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
    @allure.step("Check URL")
    def check_URL(self, uri, msg):
        expect(self.page).to_have_url(f"{host.get_base_url()}{uri}", timeout=10000), msg
    @allure.step('Element is visible')
    def check_presence(self, locator, msg):
        loc = self.page.locator(locator)
        (expect(loc).to_be_visible(visible=True, timeout=12000), msg)

    @allure.step('Element is hidden')
    def check_absence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_hidden(timeout=700), msg

    @allure.step('Element has all text')
    def have_text(self, locator, text: str, msg):
        loc = self.page.locator(locator)
        expect(loc).to_have_text(text), msg

    def to_be_empty(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_empty(), msg

    @allure.step('Element has partial text')
    def contain_text(self, locator, text: str, msg):
        loc = self.page.locator(locator)
        expect(loc).to_contain_text(text), msg

    def get_element_by_index(self, locator, index, timeout=1000):
        elements = self.page.query_selector_all(locator)
        return elements[index]

    @allure.step("Check equals")
    def check_equals(self, actual, expected, msg):
        assert actual == expected, msg
    @allure.step("Count element on page")
    def count_elements(self, locator, count: int, msg):
        elements = self.page.query_selector_all(locator)
        assert len(elements) == count, msg

    def have_title(self, locator, expected_title: str):
        actual_title = self.page.locator(locator).get_attribute("title")
        assert actual_title == expected_title
    @allure.step("Don't equal")
    def check_not_equal(self, actual, expected, msg):
        assert actual != expected, msg
