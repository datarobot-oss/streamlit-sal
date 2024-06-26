from .utils import create_markdown_container


# Text elements
def write(*args):
    return create_markdown_container('write', args)


def title(*args):
    return create_markdown_container('title', args)


def header(*args):
    return create_markdown_container('header', args)


def subheader(*args):
    return create_markdown_container('subheader', args)


def markdown(*args):
    return create_markdown_container('markdown', args)


# Formatted text elements
def caption(*args):
    return create_markdown_container('caption', args)


def code(*args):
    return create_markdown_container('code', args)


def divider(*args):
    return create_markdown_container('divider', args)


def latex(*args):
    return create_markdown_container('latex', args)


def text(*args):
    return create_markdown_container('text', args)


# Data elements
def dataframe(*args):
    return create_markdown_container('dataframe', args)


def data_editor(*args):
    return create_markdown_container('data_editor', args)


def table(*args):
    return create_markdown_container('table', args)


def metric(*args):
    return create_markdown_container('metric', args)


def json(*args):
    return create_markdown_container('json', args)


# Chart elements
def area_chart(*args):
    return create_markdown_container('area_chart', args)


def bar_chart(*args):
    return create_markdown_container('bar_chart', args)


def line_chart(*args):
    return create_markdown_container('line_chart', args)


def map(*args):
    return create_markdown_container('map', args)


def altair_chart(*args):
    return create_markdown_container('altair_chart', args)


def scatter_chart(*args):
    return create_markdown_container('scatter_chart', args)


def bokeh_chart(*args):
    return create_markdown_container('bokeh_chart', args)


def graphviz_chart(*args):
    return create_markdown_container('graphviz_chart', args)


def plotly_chart(*args):
    return create_markdown_container('plotly_chart', args)


def pydeck_chart(*args):
    return create_markdown_container('pydeck_chart', args)


def pyplot(*args):
    return create_markdown_container('pyplot', args)


def vega_lite_chart(*args):
    return create_markdown_container('vega_lite_chart', args)


# Input elements

def button(*args):
    return create_markdown_container('button', args)


def download_button(*args):
    return create_markdown_container('download_button', args)


def form_submit_button(*args):
    return create_markdown_container('form_submit_button', args)


def link_button(*args):
    return create_markdown_container('link_button', args)


def page_link(*args):
    return create_markdown_container('page_link', args)


def checkbox(*args):
    return create_markdown_container('checkbox', args)


def color_picker(*args):
    return create_markdown_container('color_picker', args)


def multiselect(*args):
    return create_markdown_container('multiselect', args)


def radio(*args):
    return create_markdown_container('radio', args)


def selectbox(*args):
    return create_markdown_container('selectbox', args)


def select_slider(*args):
    return create_markdown_container('select_slider', args)


def toggle(*args):
    return create_markdown_container('toggle', args)


def number_input(*args):
    return create_markdown_container('number_input', args)


def slider(*args):
    return create_markdown_container('slider', args)


def date_input(*args):
    return create_markdown_container('date_input', args)


def time_input(*args):
    return create_markdown_container('time_input', args)


def text_area(*args):
    return create_markdown_container('text_area', args)


def text_input(*args):
    return create_markdown_container('text_input', args)


def camera_input(*args):
    return create_markdown_container('camera_input', args)


def file_uploader(*args):
    return create_markdown_container('file_uploader', args)


# Media elements


def audio(*args):
    return create_markdown_container('audio', args)


def image(*args):
    return create_markdown_container('image', args)


def logo(*args):
    return create_markdown_container('logo', args)


def video(*args):
    return create_markdown_container('video', args)


# Layout and container elements
# TODO Add support in APP-

def columns(*args):
    return create_markdown_container('columns', args)


def column(*args):
    return create_markdown_container('column', args)


def container(*args):
    return create_markdown_container('container', args)


def dialog(*args):
    return create_markdown_container('dialog', args)


def empty(*args):
    return create_markdown_container('empty', args)


def expander(*args):
    return create_markdown_container('expander', args)


def form(*args):
    return create_markdown_container('form', args)


def popover(*args):
    return create_markdown_container('popover', args)


def sidebar(*args):
    return create_markdown_container('sidebar', args)


def tabs(*args):
    return create_markdown_container('tabs', args)


# Chat elements
def chat_input(*args):
    return create_markdown_container('chat_input', args)


def chat_message(*args):
    return create_markdown_container('chat_message', args)


# Status elements
def success(*args):
    return create_markdown_container('success', args)


def info(*args):
    return create_markdown_container('info', args)


def warning(*args):
    return create_markdown_container('warning', args)


def error(*args):
    return create_markdown_container('error', args)


def exception(*args):
    return create_markdown_container('exception', args)


def progress(*args):
    return create_markdown_container('progress', args)


def spinner(*args):
    return create_markdown_container('spinner', args)


def status(*args):
    return create_markdown_container('status', args)


def toast(*args):
    return create_markdown_container('toast', args)
