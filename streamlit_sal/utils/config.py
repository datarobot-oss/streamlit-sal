import os
from configparser import ConfigParser
from .. import CONFIG_FILE_NAME, CONFIG_DEFAULT_SECTION, ConfigOptions


def read_config():
    config = ConfigParser()
    config_file_path = find_config_file()
    config.read(config_file_path)
    return config


def update_config(key, value):
    config = read_config()
    config.set(CONFIG_DEFAULT_SECTION, key, value)
    save_config(config)


def save_config(config):
    config_file_path = find_config_file()
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)


def get_config_value(key):
    config = read_config()
    return config.get(CONFIG_DEFAULT_SECTION, key)


def find_root_dir():
    current_dir = os.getcwd()
    while True:
        config_file_path = os.path.join(current_dir, CONFIG_FILE_NAME)
        if os.path.exists(config_file_path):
            return current_dir
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            # We have reached the root directory
            break
        current_dir = parent_dir
    raise Exception(f"Could not find root directory. Did you run 'streamlit-sal init'?")


def find_config_file():
    root_dir = find_root_dir()
    config_file_path = os.path.join(root_dir, CONFIG_FILE_NAME)
    if os.path.exists(config_file_path):
        return config_file_path
    else:
        raise Exception(f"Could not locate {CONFIG_FILE_NAME}. Did you run 'streamlit-sal init'?")


def get_css_filepath():
    root_dir = find_root_dir()
    path = get_config_value(ConfigOptions.CSS_STYLESHEET_FILE_PATH.value)
    name = get_config_value(ConfigOptions.CSS_STYLESHEET_FILE_NAME.value)
    css_file_path = os.path.join(root_dir, path, name)
    return css_file_path
