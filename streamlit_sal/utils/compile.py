import os
from importlib.resources import files

import sass

from .config import get_config_value
from .. import ConfigOptions, STYLE_SASS_MAIN_FILE_NAME


def run_compile():
    # Define the input SASS file
    sass_path = get_config_value(ConfigOptions.SASS_SOURCE_PATH.value)
    input_file = os.path.join(sass_path, STYLE_SASS_MAIN_FILE_NAME)
    include_paths = [str(files(f"streamlit_sal.sass")), sass_path]

    # Define the output CSS file
    css_path = get_config_value(ConfigOptions.CSS_STYLESHEET_FILE_PATH.value)
    css_file = get_config_value(ConfigOptions.CSS_STYLESHEET_FILE_NAME.value)
    output_file = os.path.join(css_path, css_file)

    with open(output_file, 'w') as f:
        compiled_css = sass.compile(filename=input_file,
                                    include_paths=include_paths)  # TODO Consider using output_style='compressed' ?
        f.write(compiled_css)
        print(f"Compiled {input_file} to {output_file}")
