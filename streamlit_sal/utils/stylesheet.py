from contextlib import contextmanager

import streamlit as st

from .config import get_css_filepath


def sal_stylesheet(reduce_markdown_spacing=True, move_sidebar_right=False):
    css_filepath = get_css_filepath()
    try:
        with open(css_filepath, 'r') as css_file:
            css_stylesheet = css_file.read()

            if css_stylesheet:
                container = st.container()

                container.markdown(f"""
                    <style class="hidden">
                        {css_stylesheet}
                    </style>
                """, unsafe_allow_html=True)

                app_styles = []
                if reduce_markdown_spacing:
                    app_styles.append('sal-reduce-main-container-space')

                if move_sidebar_right:
                    app_styles.append('sal-move-sidebar-right')

                if len(app_styles) > 0:
                    container.markdown(f"<span class='{' '.join(app_styles)} hidden'></span>", unsafe_allow_html=True)

                return container
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not locate stylesheet: {css_filepath}")


@contextmanager
def create_markdown_container(component_name, class_names=None, is_hidden=True):
    classes = list(class_names) if class_names else []
    classes.append(f"sal-{component_name}")
    if is_hidden:
        classes.append('hidden')
    st.markdown(f"<span class='{' '.join(classes)}'></span>", unsafe_allow_html=True)
    yield
