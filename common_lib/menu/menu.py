from common_lib.menu.menu_locators import MenuLocators
from common_lib.base_page import BasePage


class Menu(BasePage):

    def click_on_button(self):
        self.click(*MenuLocators.any_button)