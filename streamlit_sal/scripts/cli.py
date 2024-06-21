import click
from click import ClickException

from ..utils import run_compile
from .init_files import run_init


@click.group()
def cli():
    pass


@cli.command()
def compile():
    run_compile()


@cli.command()
def init():
    if not click.confirm(text='Did you run this command from the project root directory?'):
        raise ClickException("Please run 'streamlit-sal init' from the project root directory")

    run_init()


if __name__ == "__main__":
    cli()
