import streamlit as st


def button(*classes):
    # Todo: Add args class name validation for st.column styles
    container = st.container()
    container.markdown(f"<span class='sal-button {' '.join(classes)} hidden'></span>", unsafe_allow_html=True)
    return container
