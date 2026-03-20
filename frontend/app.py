import streamlit as st
from products import show_products
from trends import show_trends
from layout import set_layout
from navigation import top_navigation
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
    # Spacer
    st.markdown("<div style='height: 50px'></div>", unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1, 1.8, 1])

    with col_center:
        # Animated logo
        st.markdown("""
        <div style="text-align:center; animation: fadeInUp 0.6s ease-out;">
            <div style="
                font-size: 72px;
                margin-bottom: 12px;
                animation: float 3s ease-in-out infinite;
                filter: drop-shadow(0 0 20px rgba(139,92,246,0.3));
            ">📦</div>
            <div class="hero-title" style="font-size:48px; margin-bottom:4px;">Stockify</div>
            <div class="hero-sub" style="font-size:16px; margin-bottom:40px;">
                Smart Inventory Intelligence for Modern Retailers
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Login Card
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)

        st.markdown("""
        <div class="login-title">Welcome Back 👋</div>
        <div class="login-sub">Sign in to access your command center</div>
        """, unsafe_allow_html=True)

        username = st.text_input("Email", placeholder="admin@stockify.com")
        password = st.text_input("Password", type="password", placeholder="••••••••")

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        if st.button("🚀 Sign In", use_container_width=True):
            if username == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("❌ Invalid credentials. Try admin / admin")

        st.markdown("</div>", unsafe_allow_html=True)

        # Features
        st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)

        features = [
            ("📤", "Drag & Drop CSV Upload"),
            ("⚡", "Real-Time Demand Analysis"),
            ("🎯", "Actionable Smart Recommendations"),
        ]

        for i, (icon, text) in enumerate(features):
            st.markdown(f"""
            <div class="feature-item delay-{i+2}">
                <div class="feature-icon">{icon}</div>
                <div class="feature-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)


# ---------------- MAIN APP ----------------
if not st.session_state.logged_in:
    login_page()
else:
    page = top_navigation()

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
