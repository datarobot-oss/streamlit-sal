from ..utils import create_markdown_container


def button(*args):
    return create_markdown_container('button', args)
