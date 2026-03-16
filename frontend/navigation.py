import streamlit as st

def sidebar_navigation():

    st.sidebar.markdown("## 📦 Stockify")
    st.sidebar.caption("Smart Inventory Platform")

    page = st.sidebar.radio(
        "Navigation",
        ["🏠 Home", "📂 Upload", "📊 Overview", "📦 Products", "📈 Trends", "💡 Insights"]
    )

    st.sidebar.divider()

    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    return page
