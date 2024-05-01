# simplecoin project
# For parse config from file 'config.ini'

from configparser import ConfigParser
import os

def set_config():
    config = ConfigParser()
    config_file_path = os.path.join(os.path.dirname(__file__), '../config.ini')
    config.read(config_file_path)

    return config

def get_node() -> str:
    config = set_config()
    return config['NODE']['NODE']

