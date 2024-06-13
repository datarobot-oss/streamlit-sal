import streamlit as st


def get_markdown_span_selector(key):
    """Helper to identify a specific markdown span element by the given key.
        Intended to be used together with ':has( > ...)' to find element-containers
    Parameters
    ----------
    key: str or None
        Key that uniquely identifies the custom component
        Note that providing 'None' will target ALL custom markdown spans in the app
    Returns
    -------
    str
        CSS Selector for the custom span markdown of the given key
    """
    class_str = f".{key}" if key is not None or "" else ""

    return f"""
            div.stMarkdown > div[data-testid="stMarkdownContainer"] > p > span{class_str}
        """


def remove_markdown_space():
    """Remove default gaps and margins around st.markdown components. Note: Run it at the top of your app."""

    # TODO: Once basic stylesheet is added, check if this style can move there. See ISSUE APP-2788

    st.markdown(
        f"""
        <style class="hidden">
            /*
            * Streamlit adds margins and heights to every st.markdown element, even if it doesnt contain any visible
            * elements. Hide all elements that contain a script or style tag with the 'hidden' class.
            */
            div[data-testid="element-container"]:has(> div.stMarkdown > div[data-testid="stMarkdownContainer"]
              > style.hidden),
              div[data-testid="element-container"]:has(> div.stMarkdown > div[data-testid="stMarkdownContainer"]
              > script.hidden) {{
                display: none;
            }}
            
            /* Hide the spans that help CSS selectors to find the right sibling elements. Uses class 'hidden'  */
            .element-container:has(> {get_markdown_span_selector('hidden')}) {{ 
                display: none;
            }}
        </style>
    """,
        unsafe_allow_html=True,
    )


def remove_main_container_padding():
    """Removes the empty space around main section and the large padding around block-container element.
    Note: Run it at the top of your app."""

    # TODO: Once basic stylesheet is added, check if this style can move there. See ISSUE APP-2788

    st.markdown(
        """
            <style class="hidden">
                .block-container {
                    padding: 4rem 1rem 0rem;
                    min-height: 80%;
                }
            </style>
        """,
        unsafe_allow_html=True,
    )
