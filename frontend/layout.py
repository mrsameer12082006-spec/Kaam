import streamlit as st

def set_layout():
    st.set_page_config(
        page_title="Stockify",
        page_icon="📦",
        layout="wide"
    )

    st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff; /* white background */
        color: #000000; /* black text */
    }

    section[data-testid="stSidebar"] {
        background-color: #f8fafc; /* very light sidebar */
    }

    .card {
        background-color: #ffffff; /* white card */
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb; /* light border */
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }

    .hero-title {
        font-size: 48px;
        font-weight: 700;
        text-align: center;
        color: #1f2937; /* dark title */
    }

    .hero-sub {
        text-align: center;
        color: #374151; /* dark gray subtitle */
        font-size: 18px;
    }

    .center-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
