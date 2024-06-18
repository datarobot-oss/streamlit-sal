import os
import shutil
from importlib.resources import files

from .. import CONFIG_FILE_NAME, BASE_STYLESHEET_FILE_NAME, DEFAULT_LESS_FILE_NAME, DEFAULT_CSS_FILE_NAME, ConfigOptions
from ..utils import update_config, get_config_value

LESS_PATH_MSG = "Enter a path for the LESS file. Leaving it empty will use root. "
LESS_FILE_MSG = f"Enter a name for the LESS file. Leaving it empty will use '{DEFAULT_LESS_FILE_NAME}'. "
CSS_PATH_MSG = "Enter a path for the CSS file. Leaving it empty will use root. "
CSS_FILE_MSG = f"Enter a name for the CSS file. Leaving it empty will use '{DEFAULT_CSS_FILE_NAME}'. "


def run_init():
    root_dir = os.getcwd()

    less_path = input(LESS_PATH_MSG).strip()
    less_file_name = input(LESS_FILE_MSG).strip()
    if less_file_name and '.less' not in less_file_name:
        less_file_name = f"{less_file_name}.less"

    css_path = input(CSS_PATH_MSG).strip()
    css_file_name = input(CSS_FILE_MSG).strip()
    if css_file_name and '.css' not in css_file_name:
        css_file_name = f"{css_file_name}.css"

    init_files(root_dir, less_path, less_file_name, css_path, css_file_name)


def init_files(root_dir, less_path=None, less_file_name=None, css_path=None, css_file_name=None):
    if not os.path.exists(CONFIG_FILE_NAME):
        copy_template_file(CONFIG_FILE_NAME, root_dir)

    if less_path:
        update_config(ConfigOptions.LESS_FILE_PATH.value, less_path)

    if less_file_name:
        update_config(ConfigOptions.LESS_FILE_NAME.value, less_file_name)

    if css_path:
        update_config(ConfigOptions.CSS_FILE_PATH.value, css_path)

    if css_file_name:
        update_config(ConfigOptions.CSS_FILE_NAME.value, css_file_name)

    less_destination_path = get_config_value(ConfigOptions.LESS_FILE_PATH.value)
    if less_destination_path != root_dir:
        create_directory_if_not_exists(less_destination_path)

    # Use a full path including filename to rename in case of custom name
    less_destination_path = os.path.join(less_destination_path,
                                         less_file_name if less_file_name else DEFAULT_LESS_FILE_NAME)
    copy_template_file(BASE_STYLESHEET_FILE_NAME, less_destination_path)


def copy_template_file(file_name, destination_path):
    source_file = str(files(f"streamlit_sal.templates").joinpath(file_name))
    shutil.copy(source_file, destination_path)
    print(f"Copied {source_file} to {destination_path}.")


def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory {directory_path} created.")
    else:
        print(f"Directory {directory_path} already exists.")
