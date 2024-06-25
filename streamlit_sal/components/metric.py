from ..utils import create_markdown_container


def metric(*args):
    return create_markdown_container('metric', args)
