from enum import Enum

# Stylesheet files (input/output)
STYLE_DEFAULT_DIST_DIRECTORY = '.'

STYLE_SASS_MAIN_FILE_NAME = 'main.scss'
STYLE_SASS_LAYOUT_FILE_NAME = '_layout.scss'
STYLE_SASS_UTILITIES_FILE_NAME = '_utilities.scss'
STYLE_SASS_BUILDER_FILE_NAME = '_style-builder.scss'
STYLE_SASS_ST_MAP_FILE_NAME = '_streamlit-component-map.scss'
STYLE_SASS_SOURCE_FILES = [STYLE_SASS_MAIN_FILE_NAME, STYLE_SASS_LAYOUT_FILE_NAME, STYLE_SASS_UTILITIES_FILE_NAME,
                           STYLE_SASS_BUILDER_FILE_NAME, STYLE_SASS_ST_MAP_FILE_NAME]

STYLE_DEFAULT_CSS_FILE_NAME = 'sal-stylesheet.css'

# Config util
CONFIG_FILE_NAME = '.streamlit_sal'
CONFIG_DEFAULT_SECTION = 'settings'


class ConfigOptions(Enum):
    SASS_SOURCE_PATH = 'sass_source_path'
    CSS_STYLESHEET_FILE_PATH = 'css_stylesheet_file_path'
    CSS_STYLESHEET_FILE_NAME = 'css_stylesheet_file_name'

