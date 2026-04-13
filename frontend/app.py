import sys
import os
from pathlib import Path
_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

import streamlit as st
from frontend.products import show_products
from analytics.trends import show_trends
from frontend.layout import set_layout
from frontend.navigation import top_navigation
from frontend.home import show_home
from frontend.upload import show_upload
from frontend.dashboard import show_dashboard
from analytics.insights import show_insights
from decision_support.stock_alerts import show_stock_alerts
from visualization.visualizations import show_visualizations
import sys
from pathlib import Path

# Ensure project root is in path for imports
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from analytics.analytics_runner import run_analytics
from pos.pos_page import show_pos_page

# Always run analytics fresh to ensure decision_support data is included
# This runs once per session (Streamlit caches session_state across reruns)
if "analytics_results" not in st.session_state or "stock_recommendations" not in st.session_state.get("analytics_results", {}):
    st.session_state.analytics_results = run_analytics()
# Also re-run if stock_recommendations is empty but inventory data exists
elif st.session_state.analytics_results.get("inventory_df") is not None:
    recs = st.session_state.analytics_results.get("stock_recommendations")
    if recs is None or (hasattr(recs, "empty") and recs.empty):
        st.session_state.analytics_results = run_analytics()

set_layout()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- LOGIN PAGE (Antigravity-style) ----------------
def login_page():
    # Top spacer
    st.markdown("<div style='height: 60px'></div>", unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1, 1.8, 1])

    with col_center:
        # Animated floating logo
        st.markdown("""
        <div style="text-align:center; animation: fadeInUp 0.6s cubic-bezier(.23, 1, .32, 1);">
            <div style="
                font-size: 72px;
                margin-bottom: 16px;
                animation: float 4s ease-in-out infinite;
                filter: drop-shadow(0 8px 32px rgba(50, 121, 249, 0.15));
            ">📦</div>
            <div class="hero-title-gradient" style="font-size:52px; margin-bottom:6px; letter-spacing:-2px;">Stockify</div>
            <div class="hero-sub" style="font-size:17px; margin-bottom:44px; color: #5F6368;">
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

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        # Blue pill button override for login
        st.markdown("""
        <style>
        .login-card .stButton > button {
            background: #3279F9 !important;
            color: white !important;
            border-radius: 9999px !important;
            font-size: 16px !important;
            padding: 14px 36px !important;
            font-weight: 600 !important;
            transition: all 0.4s cubic-bezier(.23, 1, .32, 1) !important;
        }
        .login-card .stButton > button:hover {
            background: #1A5CDB !important;
            box-shadow: 0 12px 36px rgba(50, 121, 249, 0.25) !important;
            transform: translateY(-2px) scale(1.03) !important;
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("🚀 Sign In", use_container_width=True):
            if username == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("❌ Invalid credentials. Try admin / admin")

        st.markdown("</div>", unsafe_allow_html=True)

        # Features section
        st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

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
    elif page == "🚨 Alerts":
        show_stock_alerts()
    elif page == "📉 Charts":
        show_visualizations()
    elif page == "💳 POS":
        show_pos_page()

