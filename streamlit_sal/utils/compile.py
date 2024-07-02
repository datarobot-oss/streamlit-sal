import os
from importlib.resources import files

import sass

from .config import get_config_value
from .. import ConfigOptions, STYLE_SASS_MAIN_FILE_NAME, STYLE_SASS_UTILITIES_FILE_NAME, STYLE_SASS_LAYOUT_FILE_NAME, \
    STYLE_SASS_BUILDER_FILE_NAME


def run_compile():
    # Define the input SASS file
    sass_path = get_config_value(ConfigOptions.SASS_SOURCE_PATH.value)
    input_file = os.path.join(sass_path, STYLE_SASS_MAIN_FILE_NAME)

    utilities_file_path = str(files(f"streamlit_sal.sass").joinpath(STYLE_SASS_UTILITIES_FILE_NAME))
    layout_file_path = str(files(f"streamlit_sal.sass").joinpath(STYLE_SASS_LAYOUT_FILE_NAME))
    style_builder_file_path = str(files(f"streamlit_sal.sass").joinpath(STYLE_SASS_BUILDER_FILE_NAME))

    # Read the template file
    try:
        with open(input_file, 'r') as template_file:
            template_content = template_file.read()

            # Replace the placeholders with the actual import statements
            filled_content = template_content.replace('// {{inject_utilities_import}}',
                                                      f"@import '{utilities_file_path}';")
            filled_content = filled_content.replace('// {{inject_layout_import}}', f"@import '{layout_file_path}';")
            filled_content = filled_content.replace('// {{inject_style_builder_import}}',
                                                    f"@import '{style_builder_file_path}';")

            # Define the output CSS file
            css_path = get_config_value(ConfigOptions.CSS_STYLESHEET_FILE_PATH.value)
            css_file = get_config_value(ConfigOptions.CSS_STYLESHEET_FILE_NAME.value)
            output_file = os.path.join(css_path, css_file)

            # Use the filled content with libsass compile
            with open(output_file, 'w') as f:
                compiled_css = sass.compile(string=filled_content)  # TODO Consider using output_style='compressed' ?
                f.write(compiled_css)
                print(f"Compiled {input_file} to {output_file}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except IOError as io_error:
        print(f"Error: {io_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
