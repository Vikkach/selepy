from allure import step
from tests.electron import TestBaseElectron


class TestDoSmthElectron(TestBaseElectron):
    def test_do_smth_with_electron(self):
        with step('Click on any button'):
            self.page_action.click_on_button()
