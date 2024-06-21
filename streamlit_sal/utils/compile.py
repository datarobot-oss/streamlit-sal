import os
import sass
from .. import ConfigOptions, STYLE_SASS_MAIN_FILE_NAME
from .config import get_config_value


def run_compile():
    # Define the input SASS file
    sass_path = get_config_value(ConfigOptions.SASS_SOURCE_PATH.value)
    input_file = os.path.join(sass_path, STYLE_SASS_MAIN_FILE_NAME)

    # Define the output CSS file
    css_path = get_config_value(ConfigOptions.CSS_STYLESHEET_FILE_PATH.value)
    css_file = get_config_value(ConfigOptions.CSS_STYLESHEET_FILE_NAME.value)
    output_file = os.path.join(css_path, css_file)

    with open(output_file, 'w') as f:
        compiled_css = sass.compile(filename=input_file)
        f.write(compiled_css)
        print(f"Compiled {input_file} to {output_file}")
