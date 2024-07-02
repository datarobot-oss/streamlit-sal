import os
import shutil
from importlib.resources import files

import click

from .. import CONFIG_FILE_NAME, STYLE_DEFAULT_CSS_FILE_NAME, \
    STYLE_DEFAULT_DIST_DIRECTORY, ConfigOptions, STYLE_SASS_MAIN_FILE_NAME
from ..utils import update_config, get_config_value

SASS_PATH_MSG = "Enter a destination path for the SASS source main file"
CSS_PATH_MSG = "Enter a destination path for the compiled CSS file output"
CSS_FILE_MSG = "Enter a file name for the compiled CSS"


def check_css_extension(file_name):
    if file_name and '.css' not in file_name:
        return f"{file_name}.css"
    else:
        return file_name


def run_init():
    root_dir = os.getcwd()

    sass_src_path = click.prompt(text=SASS_PATH_MSG, default=STYLE_DEFAULT_DIST_DIRECTORY,
                                 type=click.Path(exists=False, file_okay=False))

    path_default = sass_src_path if sass_src_path else STYLE_DEFAULT_DIST_DIRECTORY
    css_stylesheet_path = click.prompt(text=CSS_PATH_MSG, default=path_default,
                                       type=click.Path(exists=False, file_okay=False))
    css_stylesheet_file_name = click.prompt(text=CSS_FILE_MSG, default=STYLE_DEFAULT_CSS_FILE_NAME,
                                            value_proc=check_css_extension,
                                            type=click.STRING)

    init_files(root_dir, sass_src_path, css_stylesheet_path, css_stylesheet_file_name)


def init_files(root_dir, sass_src_path=None, css_stylesheet_path=None, css_stylesheet_file_name=None):
    if not os.path.exists(CONFIG_FILE_NAME):
        copy_template_file(CONFIG_FILE_NAME, root_dir)

    if sass_src_path:
        update_config(ConfigOptions.SASS_SOURCE_PATH.value, sass_src_path)

    if css_stylesheet_path:
        update_config(ConfigOptions.CSS_STYLESHEET_FILE_PATH.value, css_stylesheet_path)

    if css_stylesheet_file_name:
        update_config(ConfigOptions.CSS_STYLESHEET_FILE_NAME.value, css_stylesheet_file_name)

    sass_source_path = get_config_value(ConfigOptions.SASS_SOURCE_PATH.value)
    if sass_source_path != root_dir:
        create_directory_if_not_exists(sass_source_path)

    # Copy the main sass file to the given or default source path
    copy_template_file(STYLE_SASS_MAIN_FILE_NAME, sass_source_path)


def copy_template_file(file_name, destination_path):
    source_file = str(files(f"streamlit_sal.templates").joinpath(file_name))
    shutil.copy(source_file, destination_path)
    click.echo(f"Copied {source_file} to {destination_path}.")


def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        click.echo(f"Directory {directory_path} created.")
    else:
        click.echo(f"Directory {directory_path} already exists.")
