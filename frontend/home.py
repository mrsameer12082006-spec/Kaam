import streamlit as st

def show_home():

    st.markdown("<div class='hero-title'>Smart Inventory Decisions for Small Retailers</div>", unsafe_allow_html=True)

    st.markdown("<div class='hero-sub'>Stop relying on guesswork. Make data-driven decisions.</div>", unsafe_allow_html=True)

    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("Start Analyzing Your Data"):
        st.switch_page("upload.py")
    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("## The Problem")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>Overstocking</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'>Stock Shortages</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'>Reduced Profit</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("## Our Solution")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>Easy Upload</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'>Instant Analysis</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'>Visual Insights</div>", unsafe_allow_html=True)
