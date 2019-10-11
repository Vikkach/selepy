from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.config_parser import ConfigParser


class Driver:
    @staticmethod
    def get_driver():
        ui_config = ConfigParser('config/ui.ini').config
        application_binary_path = ui_config.get('application_binary_path', 'binary_path')

        opt = Options()
        opt.binary_location = application_binary_path
        return webdriver.Chrome(ChromeDriverManager().install(), options=opt)
