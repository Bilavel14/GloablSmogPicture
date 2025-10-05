import streamlit as st
from pathlib import Path

# --- Page settings ---
st.set_page_config(page_title="Air Quality Dashboard",
                   layout="wide")

# --- Load HTML dashboard ---
html_path = Path("index.html")
if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")
    st.components.v1.html(html_content, height=2200, scrolling=True)
else:
    st.error("index.html not found. Please add it to the project folder.")
