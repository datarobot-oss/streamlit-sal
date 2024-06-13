import streamlit as st

def move_st_sidebar_right():
    """Helper to flip the Streamlit sidebar to the right side of the view. Note: Run it at the top of your app.
    Parameters
    ----------
    Returns
    -------
    """

    # TODO: Once basic stylesheet is added, check if this style can move there. See ISSUE APP-2788

    if 'moved_st_sidebar_right' not in st.session_state:
        st.session_state['moved_st_sidebar_right'] = True

    style_text = f"""
        <style class='hidden'>
            header[data-testid="stHeader"] {{
                z-index: 991;
            }}
            
            div[data-testid="collapsedControl"] {{
                top: 3rem;
                right: 0.25rem;
                left: auto;
                height: 100%;
                z-index: 990;
            }}
            
            div[data-testid="collapsedControl"] > button {{
                transform: scaleX(-1)
            }}
            
            div.appview-container section[data-testid="stSidebar"]:first-child {{
                top: 3rem;
                order: 2;
                transform: none;
                transition: transform 300ms ease 0s, min-width 300ms ease 0s, max-width 300ms ease 0s;
                z-index: 990;
            }}

            div.appview-container section[data-testid="stSidebar"]:nth-child(2) {{
                top: 3rem;
                order: 2;
                transform: translateX(+336px);
                transition: transform 300ms ease 0s, min-width 300ms ease 0s, max-width 300ms ease 0s;
                z-index: 990;
            }}
            
            @media only screen and (max-width: 767px) {{
              div.appview-container {{
                    place-content: flex-end;
                }}
            }}

            div.appview-container div[data-testid="stSidebarContent"] + div > div {{
                /*Hides the sidebar resize handle, it cannot function properly when flipped to the right*/
                display: none;
            }}
        </style>
    """
    st.markdown(style_text, unsafe_allow_html=True)
