import streamlit as st

def top_navigation():
    """Render a premium horizontal top navigation bar."""

    if "current_page" not in st.session_state:
        st.session_state.current_page = "🏠 Home"

    pages = [
        ("🏠", "Home"),
        ("📂", "Upload"),
        ("📊", "Overview"),
        ("📦", "Products"),
        ("📈", "Trends"),
        ("💡", "Insights"),
    ]

    # Build columns: brand + pages + logout
    cols = st.columns([1.4] + [1] * len(pages) + [0.9])

    # Brand
    with cols[0]:
        st.markdown(
            "<div class='nav-brand'>📦 Stockify</div>",
            unsafe_allow_html=True,
        )

    # Nav buttons with active/inactive styling
    for i, (icon, label) in enumerate(pages):
        full_label = f"{icon} {label}"
        col_index = i + 2  # 1-indexed for CSS nth-child

        with cols[i + 1]:
            is_active = st.session_state.current_page == full_label

            if is_active:
                st.markdown(f"""
                <style>
                div[data-testid="stHorizontalBlock"] > div:nth-child({col_index}) .stButton > button {{
                    background: linear-gradient(135deg, #8b5cf6, #6d28d9) !important;
                    box-shadow: 0 6px 24px rgba(139,92,246,0.3), 0 0 0 1px rgba(139,92,246,0.2) !important;
                    border-bottom: 3px solid #a78bfa !important;
                    color: white !important;
                }}
                </style>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <style>
                div[data-testid="stHorizontalBlock"] > div:nth-child({col_index}) .stButton > button {{
                    background: rgba(255,255,255,0.03) !important;
                    border: 1px solid rgba(255,255,255,0.06) !important;
                    color: rgba(244,244,245,0.5) !important;
                }}
                div[data-testid="stHorizontalBlock"] > div:nth-child({col_index}) .stButton > button:hover {{
                    background: rgba(139,92,246,0.1) !important;
                    border-color: rgba(139,92,246,0.3) !important;
                    color: #e2e8f0 !important;
                    box-shadow: 0 4px 20px rgba(139,92,246,0.15) !important;
                }}
                </style>
                """, unsafe_allow_html=True)

            if st.button(f"{icon} {label}", key=f"nav_{label}", use_container_width=True):
                st.session_state.current_page = full_label
                st.rerun()

    # Logout button (red accent)
    logout_col_index = len(pages) + 2
    with cols[-1]:
        st.markdown(f"""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child({logout_col_index}) .stButton > button {{
            background: rgba(251,113,133,0.08) !important;
            border: 1px solid rgba(251,113,133,0.2) !important;
            color: #fb7185 !important;
        }}
        div[data-testid="stHorizontalBlock"] > div:nth-child({logout_col_index}) .stButton > button:hover {{
            background: rgba(251,113,133,0.18) !important;
            border-color: rgba(251,113,133,0.4) !important;
            box-shadow: 0 4px 24px rgba(251,113,133,0.15) !important;
        }}
        </style>
        """, unsafe_allow_html=True)
        if st.button("🚪 Logout", key="nav_logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.current_page = "🏠 Home"
            st.rerun()

    # Separator
    st.markdown(
        "<hr style='margin: 6px 0 28px 0; border-top: 1px solid rgba(255,255,255,0.04);'>",
        unsafe_allow_html=True,
    )

    return st.session_state.current_page
