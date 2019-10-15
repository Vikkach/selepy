import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.config_parser import ConfigParser
from common_lib.config_wrapper import Config


class Driver:
    def get_driver(self):
        try:
            browser = os.environ['BROWSER']
            return self.get_web_driver(browser)
        except KeyError:
            return self.get_electron_driver()

    @staticmethod
    def get_electron_driver():
        opt = Options()
        application_binary_path = Config().get_electron_binary_path()
        opt.binary_location = application_binary_path
        return webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    @staticmethod
    def get_web_driver(browser):
        if browser == 'chrome':
            opt = Options()
            opt.set_headless()
            return webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        elif browser == 'firefox':
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
