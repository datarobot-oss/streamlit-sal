import streamlit as st
import streamlit_sal as sal
from streamlit_sal import sal_stylesheet


with sal_stylesheet(reduce_markdown_spacing=True, move_sidebar_right=True):
    st.header('Example app for SAL')
    st.subheader('Remember to run `streamlit-sal compile` before running this example app')

    with sal.button():
        st.button('Custom Styled button')

    with st.sidebar:
        st.write('Sup')
