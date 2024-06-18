from enum import Enum

BASE_STYLESHEET_FILE_NAME = 'base-stylesheet.less'
DEFAULT_LESS_FILE_NAME = 'sal-stylesheet.less'
DEFAULT_CSS_FILE_NAME = 'sal-stylesheet.css'
CONFIG_FILE_NAME = '.streamlit_sal'
CONFIG_DEFAULT_SECTION = 'settings'


class ConfigOptions(Enum):
    LESS_FILE_PATH = 'less_file_path'
    LESS_FILE_NAME = 'less_file_name'
    CSS_FILE_PATH = 'css_file_path'
    CSS_FILE_NAME = 'css_file_name'

