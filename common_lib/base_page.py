from common_lib.base_logger import BaseLogger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from common_lib.general_data import TIMEOUT_SEC, SHORT_TIMEOUT_SEC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_visible(self, locator, timeout=TIMEOUT_SEC):
        try:
            _d = self.driver
            WebDriverWait(_d, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Element {locator} missed. It takes more than {timeout} sec to load an element')

    def click(self, *locator):
        BaseLogger.get_info_log(f'Click on element with locator {locator}')
        self.wait_until_element_to_be_clickable(locator)
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        """
        Wait until element is visible and find an element.
        :param locator: an element given a By strategy and locator. E.g. (By.XPATH, '//input[@id="username"]')
        :return: WebElement
        """
        BaseLogger.get_info_log(f'Find element with locator {locator}')
        self.wait_until_element_is_visible(locator)
        return self.driver.find_element(*locator)

    def wait_until_element_to_be_clickable(self, *locator, timeout=TIMEOUT_SEC):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(*locator))
        except TimeoutException:
            raise AssertionError(f'Cannot click on element {locator}. It takes more than {timeout} sec to wait')

    def type_with_hover_and_click(self, text, *locator):
        """
        Hover on WebElement, click on it to enable and enter text
        :param text: input text
        :param locator: an element given a By strategy and locator. E.g. (By.XPATH, '//input[@id="username"]')
        """
        self.hover(*locator)
        self.click(*locator)
        self.type(text, *locator)

    def type(self, text, *locator):
        element = self.driver.find_element(*locator)
        BaseLogger.get_info_log(f'Type {text} into field with locator {locator}')
        element.send_keys(text)

    def hover(self, *locator):
        """
        Hove on WebElement
        :param locator: an element given a By strategy and locator. E.g. (By.XPATH, '//input[@id="username"]')
        """
        BaseLogger.get_info_log(f'Hove on element with locator {locator}')
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_element_presence(self, *locator):
        try:
            self.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def find_elements(self, *locator):
        """
        Find elements by locator. Useful for table, lists, drop-downs, etc.
        :param locator: an element given a By strategy and locator. E.g. (By.XPATH, '//input[@id="username"]')
        :return: list of WebElement
        """
        return self.driver.find_elements(*locator)

    def wait_until_element_present(self, *locator):
        try:
            # wait for loading element to appear
            # - required to prevent prematurely checking if element
            #   has disappeared, before it has had a chance to appear
            WebDriverWait(self.driver, SHORT_TIMEOUT_SEC).until(EC.presence_of_element_located(*locator))

            # then wait for the element to disappear
            WebDriverWait(self.driver, TIMEOUT_SEC).until_not(EC.presence_of_element_located(*locator))

        except TimeoutException:
            pass
