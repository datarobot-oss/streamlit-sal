import streamlit as st
import streamlit_sal as sal
from streamlit_sal import sal_stylesheet


with sal_stylesheet():
    st.header('Example app for SAL')

    with sal.button():
        st.button('Custom Styled button')