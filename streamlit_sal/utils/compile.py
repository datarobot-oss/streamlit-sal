import os
from importlib.resources import files

import sass
import streamlit as st

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
        variables_css = generate_st_theme_variables_css()
        f.write(variables_css + '\n' + compiled_css)
        print(f"Compiled {input_file} to {output_file}")


def generate_st_theme_variables_css():
    primary_color = st.get_option('theme.primaryColor')
    background_color = st.get_option('theme.backgroundColor')
    secondary_background_color = st.get_option('theme.secondaryBackgroundColor')
    text_color = st.get_option('theme.textColor')
    font = st.get_option('theme.font')
    base = st.get_option('theme.base')

    css_vars = [
        f'--st-primary-color: {primary_color};' if primary_color is not None else '',
        f'--st-background-color: {background_color};' if background_color is not None else '',
        f'--st-secondary-background-color: {secondary_background_color};' if secondary_background_color is not None else '',
        f'--st-text-color: {text_color};' if text_color is not None else '',
        f'--st-font: {font};' if font is not None else '',
        f'--st-theme-base: {base};' if base is not None else ''
    ]

    # Ignore any empty string vars
    css_vars_no_empty_str = [var for var in css_vars if var]

    if len(css_vars_no_empty_str) > 0:
        # Join the variables with a newline character
        css_vars_str = "\n  ".join(css_vars_no_empty_str)

        return (
            ":root {\n"
            f"  {css_vars_str}\n"
            "}"
        )

    return ''
