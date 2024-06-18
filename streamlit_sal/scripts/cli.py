import sys
from ..utils import run_compile
from .init_files import run_init


def prompt_yes_no(message):
    while True:
        user_input = input(f"{message} (y/n): ").strip().lower()
        if user_input in ('y', 'yes'):
            return True
        elif user_input in ('n', 'no'):
            return False
        else:
            print("Invalid input. Please enter 'y/yes' or 'n/no'.")


def prompt_string(message):
    while True:
        user_input = input(f"{message}: ").strip().lower()
        if user_input in ('y', 'yes'):
            return True
        elif user_input in ('n', 'no'):
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else None
    args = sys.argv[2:]

    if command == "init":
        if prompt_yes_no("Did you run this command from the project root?"):
            run_init()
        else:
            print("Please run 'init' again from the project root directory")
    elif command == "compile":
        run_compile()
    else:
        print("Unknown command. Please try again, see documentation at: X")  # TODO PASTE LINK


if __name__ == "__main__":
    main()
