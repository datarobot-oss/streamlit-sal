from .utils import create_markdown_container


def validate_container_kwarg(component_name, **kwargs):
    if 'container' not in kwargs:
        print(
            f"[INFO] Pass the layout container from your st.{component_name} call to SAL. Read more here: https://github.com/datarobot/streamlit-sal/blob/main/README.md")
        raise TypeError(f"(sal.{component_name}) Missing required keyword argument: 'container'")
    pass


# Text elements
def write(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='write')


def title(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='title')


def header(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='header')


def subheader(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='subheader')


def markdown(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='markdown')


# Formatted text elements
def caption(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='caption')


def code(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='code')


def divider(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='divider')


def latex(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='latex')


def text(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='text')


# Data elements
def dataframe(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='dataframe')


def data_editor(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='data_editor')


def table(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='table')


def metric(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='metric')


def json(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='json')


# Chart elements
def area_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='area_chart')


def bar_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='bar_chart')


def line_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='line_chart')


def map(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='map')


def altair_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='altair_chart')


def scatter_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='scatter_chart')


def bokeh_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='bokeh_chart')


def graphviz_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='graphviz_chart')


def plotly_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='plotly_chart')


def pydeck_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='pydeck_chart')


def pyplot(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='pyplot')


def vega_lite_chart(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='vega_lite_chart')


# Input elements

def button(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='button')


def download_button(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='download_button')


def form_submit_button(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='form_submit_button')


def link_button(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='link_button')


def page_link(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='page_link')


def checkbox(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='checkbox')


def color_picker(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='color_picker')


def multiselect(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='multiselect')


def radio(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='radio')


def selectbox(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='selectbox')


def select_slider(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='select_slider')


def toggle(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='toggle')


def number_input(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='number_input')


def slider(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='slider')


def date_input(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='date_input')


def time_input(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='time_input')


def text_area(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='text_area')


def text_input(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='text_input')


def camera_input(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='camera_input')


def file_uploader(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='file_uploader')


# Media elements


def audio(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='audio')


def image(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='image')


def logo(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='logo')


def video(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='video')


# Layout and container elements
def columns(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='columns')


def column(*args, **kwargs):
    # Column element has to pass its container for the span identifier
    validate_container_kwarg('column', **kwargs)
    return create_markdown_container(*args, **kwargs, component_name='column')


def container(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='container')


def dialog(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='dialog')


def empty(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='empty')


def expander(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='expander')


def form(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='form')


def popover(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='popover')


def popover_content(*args, **kwargs):
    # Popover element has to pass its container for the span identifier
    validate_container_kwarg('popover_content', **kwargs)
    return create_markdown_container(*args, **kwargs, component_name='popover_content')


def sidebar(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='sidebar')


def tabs(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='tabs')


# Chat elements
def chat_input(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='chat_input')


def chat_message(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='chat_message')


# Status elements
def success(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='success')


def info(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='info')


def warning(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='warning')


def error(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='error')


def exception(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='exception')


def progress(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='progress')


def spinner(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='spinner')


def status(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='status')


def toast(*args, **kwargs):
    return create_markdown_container(*args, **kwargs, component_name='toast')
