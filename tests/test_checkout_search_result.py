import pytest
from pages.overview_main_page import OverviewPage

@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestCheckoutSearchResult:
    def test_checkout_search_result(self, browser):
        overview = OverviewPage(browser)
        overview.fill_data_and_goto_results()
        overview.check_results_searching()
        overview.click_project_card()