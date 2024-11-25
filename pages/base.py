from playwright.sync_api import Page, TimeoutError, Response
from data.environment import host
import allure

class Base:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open URL")
    def open(self, uri) -> Response | None:
        return self.page.goto(f"{host.get_base_url()}{uri}", wait_until='domcontentloaded')

    @allure.step("Input")
    def input(self, locator, data: str) -> None:
        self.page.locator(locator).fill(data)

    @allure.step("Click to button")
    def click(self, locator) -> None:
        self.page.click(locator)

    def get_text(self, locator: str, index: int) -> str:
        return self.page.locator(locator).nth(index).text_content()

    @allure.step("Click by element with index")
    def click_element_by_index(self, selector: str, index: int):
        self.page.locator(selector).nth(index).click()

    @allure.step("Input data with index")
    def input_value_by_index(self, selector: str, index: int, data: str):  # вводим данные в нужные поля по индексу
        self.page.locator(selector).nth(index).fill(data)

    @allure.step("Click first element on page")
    def click_first_element(self, locator: str):
        self.page.locator(locator).first.click()

    @allure.step("Get element by index")
    def get_element_by_index(self, locator, index):
        locator = self.page.locator(locator)
        return locator.nth(index)

    def wait_for_element(self, locator, timeout=12000) -> None:
        self.page.wait_for_selector(locator, timeout=timeout)

    def click_by_text(self, text: str):
        self.page.get_by_text(text).click()

    @allure.step("Refresh page")
    def refresh(self) -> Response | None:
        return self.page.reload(wait_until='domcontentloaded')

    @allure.step("Get element in nested elements")
    def get_text_element_by_index_all_elements(self, selector, selector2, index):
        element = self.page.query_selector(selector)

        elements = element.query_selector_all(selector2)

        if len(elements) == 0:
            raise ValueError("No elements found for the given selector")
        return elements[index]
