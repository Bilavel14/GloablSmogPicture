import streamlit as st
from pathlib import Path

st.set_page_config(page_title="NDMA – Air Quality Dashboards", layout="wide")

html_file = Path("index.html")
if html_file.exists():
    st.components.v1.html(html_file.read_text(encoding="utf-8"), height=2200, scrolling=True)
else:
    st.error("index.html not found.")
