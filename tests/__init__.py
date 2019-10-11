import pytest
from common_lib.driver_wrapper import Driver
from common_lib.menu.menu import Menu


class TestBaseUI:
    driver = None

    def setup_class(self):
        self.driver = Driver.get_driver()
        self.menu_action = Menu(self.driver)

    def teardown_class(self):
        self.driver.quit()
