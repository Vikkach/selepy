
from common_lib.driver_wrapper import Driver
from common_lib.page.page import Page


class TestBaseUI:
    driver = None

    def setup_class(self):
        driver = Driver()
        self.driver = driver.get_driver()
        self.page_action = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()
