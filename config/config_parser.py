import configparser
import os


class ConfigParser:
    def __init__(self, path):
        self.config_path = os.path.expanduser('{}{}'.format(os.getcwd(), path))
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read(path)
