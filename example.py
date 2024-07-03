import streamlit as st

import streamlit_sal as sal
from streamlit_sal import sal_stylesheet

with sal_stylesheet():
    st.header('Example app for SAL')
    st.subheader('Remember to run `streamlit-sal compile` before running this example app')

    # TODO: Clean up after APP-2789
    with sal.write():
        st.write('This should be blue text')

    with sal.metric():
        st.metric("Temperature", "70 °F", "1.2 °F")

    st.write('A styled button with pink border and color')
    with sal.button():
        st.button('Default SAL button')

    st.write('A styled button with pink border and color. Has custom class button-large')
    with sal.button('button-large'):
        st.button('Custom large pink SAL button')

    st.write('A styled button with pink border and color. Has custom class button-large AND button-disabled')
    with sal.button('button-large', 'button-disabled'):
        st.button('Custom large & disabled pink SAL button')

    with st.sidebar:
        st.write('The sidebar is on the right side due to move_sidebar_right=True in `with sal_stylesheet(..)`')
