from contextlib import contextmanager

import streamlit as st

from .config import get_css_filepath


@contextmanager
def sal_stylesheet(move_sidebar_right=False, reduce_main_container_space=False):
    css_filepath = get_css_filepath()
    try:
        with open(css_filepath, 'r') as css_file:
            css_stylesheet = css_file.read()

            if css_stylesheet:
                st.markdown(f"""
                    <style class="hidden">
                        {css_stylesheet}
                    </style>
                """, unsafe_allow_html=True)

                app_styles = []
                if reduce_main_container_space:
                    app_styles.append('sal-reduce-main-container-space')

                if move_sidebar_right:
                    app_styles.append('sal-move-sidebar-right')

                if len(app_styles) > 0:
                    st.markdown(f"<span class='{' '.join(app_styles)} hidden'></span>", unsafe_allow_html=True)
            yield
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not locate stylesheet: {css_filepath}")


@contextmanager
def create_markdown_container(*args, **kwargs):
    is_hidden = kwargs.pop('is_hidden', True)
    container = kwargs.pop('container') if 'container' in kwargs else None
    component_name = kwargs.pop('component_name') if 'component_name' in kwargs else None
    if component_name is None:
        raise ValueError(f"component_name has to be defined.")

    # Replace any name underscores with dash to match class naming conventions in the style placeholders
    component_name = component_name.replace("_", "-")
    classes = list(args) if args else []
    classes.append(f"sal-{component_name}")
    if is_hidden:
        classes.append('hidden')
    if container:
        container.markdown(f"<span class='{' '.join(classes)}'></span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span class='{' '.join(classes)}'></span>", unsafe_allow_html=True)
    yield
