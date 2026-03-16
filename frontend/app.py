import streamlit as st
from products import show_products
from trends import show_trends
from layout import set_layout
from navigation import sidebar_navigation
from home import show_home
from upload import show_upload
from dashboard import show_dashboard
from insights import show_insights
import sys
from pathlib import Path

# Ensure project root is in path for imports
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from analytics.analytics_runner import run_analytics

@st.cache_data
def get_analytics_results():
    return run_analytics()

# Run analytics and store in session state
if "analytics_results" not in st.session_state:
    st.session_state.analytics_results = get_analytics_results()

set_layout()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- LOGIN PAGE ----------------
def login_page():

    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown("## 📦 Stockify")
        st.markdown("### Smart Inventory Management for Small Retailers")
        st.markdown(
            "Make data-driven inventory decisions with simple, affordable analytics."
        )

        st.markdown("""
        ✔ Easy CSV Upload  
        ✔ Instant Demand Analysis  
        ✔ Actionable Recommendations  
        """)

    with col2:
        st.markdown("### Welcome Back")

        username = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Sign In", use_container_width=True):
            if username == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid credentials")


# ---------------- MAIN APP ----------------
if not st.session_state.logged_in:
    login_page()
else:
    page = sidebar_navigation()

    if page == "🏠 Home":
        show_home()
    elif page == "📂 Upload":
        show_upload()
    elif page == "📊 Overview":
        show_dashboard()
    elif page == "📦 Products":
        show_products()
    elif page == "📈 Trends":
        show_trends()
    elif page == "💡 Insights":
        show_insights()
