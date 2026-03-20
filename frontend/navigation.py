import streamlit as st

def top_navigation():
    """Render an Antigravity-style frosted glass top navigation bar."""

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

    # Nav buttons with Antigravity active/inactive styling
    for i, (icon, label) in enumerate(pages):
        full_label = f"{icon} {label}"
        col_index = i + 2  # 1-indexed for CSS nth-child

        with cols[i + 1]:
            is_active = st.session_state.current_page == full_label

            if is_active:
                st.markdown(f"""
                <style>
                div[data-testid="stHorizontalBlock"] > div:nth-child({col_index}) .stButton > button {{
                    background: #3279F9 !important;
                    color: white !important;
                    border-radius: 9999px !important;
                    box-shadow: 0 4px 16px rgba(50, 121, 249, 0.2) !important;
                    border: none !important;
                    font-weight: 600 !important;
                }}
                </style>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <style>
                div[data-testid="stHorizontalBlock"] > div:nth-child({col_index}) .stButton > button {{
                    background: transparent !important;
                    border: 1px solid rgba(0, 0, 0, 0.06) !important;
                    color: #5F6368 !important;
                    border-radius: 9999px !important;
                }}
                div[data-testid="stHorizontalBlock"] > div:nth-child({col_index}) .stButton > button:hover {{
                    background: rgba(50, 121, 249, 0.06) !important;
                    border-color: rgba(50, 121, 249, 0.15) !important;
                    color: #3279F9 !important;
                    box-shadow: 0 4px 16px rgba(50, 121, 249, 0.08) !important;
                }}
                </style>
                """, unsafe_allow_html=True)

            if st.button(f"{icon} {label}", key=f"nav_{label}", use_container_width=True):
                st.session_state.current_page = full_label
                st.rerun()

    # Logout button (red accent, pill style)
    logout_col_index = len(pages) + 2
    with cols[-1]:
        st.markdown(f"""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child({logout_col_index}) .stButton > button {{
            background: rgba(217, 48, 37, 0.06) !important;
            border: 1px solid rgba(217, 48, 37, 0.12) !important;
            color: #D93025 !important;
            border-radius: 9999px !important;
        }}
        div[data-testid="stHorizontalBlock"] > div:nth-child({logout_col_index}) .stButton > button:hover {{
            background: rgba(217, 48, 37, 0.12) !important;
            border-color: rgba(217, 48, 37, 0.25) !important;
            box-shadow: 0 4px 16px rgba(217, 48, 37, 0.1) !important;
        }}
        </style>
        """, unsafe_allow_html=True)
        if st.button("🚪 Logout", key="nav_logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.current_page = "🏠 Home"
            st.rerun()

    # Separator
    st.markdown(
        "<hr style='margin: 8px 0 32px 0; border-top: 1px solid rgba(0, 0, 0, 0.05);'>",
        unsafe_allow_html=True,
    )

    return st.session_state.current_page
