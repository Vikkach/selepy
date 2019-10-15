from allure import step
from tests.web import TestBaseWeb


class TestDoSmthWeb(TestBaseWeb):
    def test_do_smth_with_web(self):
        with step('Go to wikipedia.org'):
            self.page_action.open_page()
        with step('Click on any button'):
            self.page_action.click_on_button()
