"""Xiaobu Chinese: a Chinese (HSK 1 and HSK 2) learning app.

This Streamlit page shows the app in xiaobu.html full-screen.
All lessons, sound, flashcards, quizzes and grammar live in xiaobu.html.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Xiaobu Chinese",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own header, footer and padding so the app fills the screen.
st.markdown(
    """
    <style>
      #MainMenu, footer, header, [data-testid="stHeader"],
      [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

APP_HTML = (Path(__file__).parent / "xiaobu.html").read_text(encoding="utf-8")

# Makes the embedded app as tall as the browser window, so it scrolls in one place.
FIT_TO_WINDOW = """
<script>
(function () {
  function fit() {
    try { window.frameElement.style.height = window.parent.innerHeight + 'px'; } catch (e) {}
  }
  fit();
  try { window.parent.addEventListener('resize', fit); } catch (e) {}
})();
</script>
"""

components.html(APP_HTML.replace("</body>", FIT_TO_WINDOW + "</body>"), height=800, scrolling=True)
