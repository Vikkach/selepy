from common_lib.page.page_locators import PageLocators
from common_lib.base_page import BasePage


class Page(BasePage):

    def click_on_button(self):
        self.click(*PageLocators.any_button)