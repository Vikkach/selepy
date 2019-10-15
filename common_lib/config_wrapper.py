import os
import configparser
from config.config_parser import ConfigParser


class Config:

    def get_main_url_from_config(self):
        try:
            common_config = self.get_config()
            return common_config.get('main_url', 'main_url')
        except configparser.NoSectionError:
            return ''

    @staticmethod
    def get_config():
        try:
            browser = os.environ['BROWSER']
            return ConfigParser('/web.ini').config
        except KeyError:
            return ConfigParser('/electron.ini').config

    @staticmethod
    def get_electron_binary_path():
        ui_config = ConfigParser('/electron.ini').config
        return ui_config.get('application_binary_path', 'binary_path')
