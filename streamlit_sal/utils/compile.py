import os
import subprocess
from .. import ConfigOptions
from .config import get_config_value


def run_compile():
    # Define the input LESS file
    less_path = get_config_value(ConfigOptions.LESS_FILE_PATH.value)
    less_file = get_config_value(ConfigOptions.LESS_FILE_NAME.value)
    input_file = os.path.join(less_path, less_file)

    # Define the output CSS file
    css_path = get_config_value(ConfigOptions.CSS_FILE_PATH.value)
    css_file = get_config_value(ConfigOptions.CSS_FILE_NAME.value)
    output_file = os.path.join(css_path, css_file)

    # Define the lessc command
    lessc_command = [
        'lessc',
        input_file,
        output_file
    ]

    # Run the lessc command
    try:
        subprocess.run(lessc_command, check=True)
        print(f"Compiled {input_file} to {output_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {input_file}: {e}")
