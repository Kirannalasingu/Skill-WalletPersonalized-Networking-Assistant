import streamlit as st

st.set_page_config(
    page_title="Test",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.title("Sidebar")
    st.write("Hello")

st.title("Main Page")