from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Good Egg",
    page_icon="\U0001F95A",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip Streamlit's default chrome and padding so the site fills the page.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] {background: #14150f;}
      [data-testid="stHeader"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).parent.joinpath("a-good-egg.html").read_text(encoding="utf-8")

# Tall height + internal scrolling so the full landing page renders in the iframe.
components.html(html, height=5200, scrolling=True)
