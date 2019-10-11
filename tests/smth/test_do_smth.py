from allure import step
from tests.smth import TestBaseRegisterHotel


class TestDoSmth(TestBaseRegisterHotel):
    def test_do_smth(self):
        with step('Click on any button'):
            self.menu_action.click_on_button()
