import streamlit as st
from .config import get_css_filepath


def sal_stylesheet():
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

                return container
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not locate stylesheet: {css_filepath}")