import streamlit as st

def show_home():
    # ===== HERO SECTION (Antigravity-style large heading) =====
    st.markdown("""
    <div style="text-align:center; margin-bottom:12px; animation: float 4s ease-in-out infinite;">
        <span style="
            font-size:64px;
            filter: drop-shadow(0 8px 32px rgba(50, 121, 249, 0.15));
        ">📦</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-title" style="font-size:68px; letter-spacing:-3px;">
        Smart Inventory Decisions<br>for Small Retailers
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-sub">
        Stop relying on guesswork. Harness the power of data to optimize stock levels,<br>
        maximize revenue, and eliminate waste.
    </div>
    """, unsafe_allow_html=True)

    # CTA Buttons (Antigravity pill-style)
    col1, col2, col3 = st.columns([1.2, 1.2, 1.2])
    with col2:
        st.markdown("""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button {
            background: #3279F9 !important;
            color: white !important;
            animation: pulse 3s ease-in-out infinite !important;
            font-size: 16px !important;
            padding: 16px 40px !important;
            border-radius: 9999px !important;
            font-weight: 600 !important;
            letter-spacing: 0.3px !important;
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button:hover {
            background: #1A5CDB !important;
            box-shadow: 0 12px 40px rgba(50, 121, 249, 0.25) !important;
        }
        </style>
        """, unsafe_allow_html=True)
        if st.button("🚀 Start Analyzing", use_container_width=True):
            st.session_state.current_page = "📂 Upload"
            st.rerun()

    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

    # ===== STATS BAR (Antigravity clean style) =====
    st.markdown("""
    <div style="
        display: flex;
        justify-content: center;
        gap: 48px;
        padding: 28px 32px;
        background: #F8F9FC;
        border-radius: 24px;
        border: 1px solid rgba(0, 0, 0, 0.06);
        animation: fadeInUp 0.7s cubic-bezier(.23, 1, .32, 1) 0.3s backwards;
        margin-bottom: 56px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    ">
        <div style="text-align:center;">
            <div style="font-size:32px; font-weight:700; color:#3279F9; letter-spacing:-1px;">10x</div>
            <div style="font-size:12px; color:#9AA0A6; text-transform:uppercase; letter-spacing:1.5px; font-weight:600; margin-top:4px;">Faster Insights</div>
        </div>
        <div style="width:1px; background:rgba(0,0,0,0.06);"></div>
        <div style="text-align:center;">
            <div style="font-size:32px; font-weight:700; color:#1E8E3E; letter-spacing:-1px;">30%</div>
            <div style="font-size:12px; color:#9AA0A6; text-transform:uppercase; letter-spacing:1.5px; font-weight:600; margin-top:4px;">Less Waste</div>
        </div>
        <div style="width:1px; background:rgba(0,0,0,0.06);"></div>
        <div style="text-align:center;">
            <div style="font-size:32px; font-weight:700; color:#7B61FF; letter-spacing:-1px;">2x</div>
            <div style="font-size:12px; color:#9AA0A6; text-transform:uppercase; letter-spacing:1.5px; font-weight:600; margin-top:4px;">Profit Growth</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===== THE PROBLEM =====
    st.markdown('<div class="section-header">😰 The Problem</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    problems = [
        ("📦", "Overstocking", "Excess inventory ties up capital and increases waste, eating into your margins.", "rgba(217,48,37,0.06)", "rgba(217,48,37,0.12)"),
        ("🚫", "Stock Shortages", "Running out of key items means lost sales and frustrated customers who won't return.", "rgba(249,171,0,0.06)", "rgba(249,171,0,0.12)"),
        ("📉", "Reduced Profit", "Without data, pricing and ordering decisions consistently leave money on the table.", "rgba(50,121,249,0.06)", "rgba(50,121,249,0.12)"),
    ]

    for i, (col, (icon, title, desc, bg, border_bg)) in enumerate(zip([col1, col2, col3], problems)):
        with col:
            st.markdown(f"""
            <div class="glass-card delay-{i+1}" style="text-align:center; min-height:210px;">
                <div style="
                    font-size:44px; margin-bottom:16px;
                    width:72px; height:72px;
                    display:inline-flex; align-items:center; justify-content:center;
                    background:{bg}; border-radius:20px;
                    border: 1px solid {border_bg};
                ">{icon}</div>
                <div style="font-size:18px; font-weight:700; color:#121317; margin-bottom:10px;">{title}</div>
                <div style="font-size:14px; color:#5F6368; line-height:1.7;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:48px'></div>", unsafe_allow_html=True)

    # ===== OUR SOLUTION =====
    st.markdown('<div class="section-header">✨ Our Solution</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    solutions = [
        ("📤", "Easy Upload", "Simply drag & drop your CSV files — inventory and sales data processed in seconds.", "rgba(50,121,249,0.06)", "rgba(50,121,249,0.12)"),
        ("⚡", "Instant Analysis", "Powerful analytics engine calculates KPIs, trends, and demand patterns automatically.", "rgba(123,97,255,0.06)", "rgba(123,97,255,0.12)"),
        ("🎯", "Visual Insights", "Beautiful charts and actionable recommendations to guide your next business move.", "rgba(30,142,62,0.06)", "rgba(30,142,62,0.12)"),
    ]

    for i, (col, (icon, title, desc, bg, border_bg)) in enumerate(zip([col1, col2, col3], solutions)):
        with col:
            st.markdown(f"""
            <div class="glass-card delay-{i+3}" style="text-align:center; min-height:210px;">
                <div style="
                    font-size:44px; margin-bottom:16px;
                    width:72px; height:72px;
                    display:inline-flex; align-items:center; justify-content:center;
                    background:{bg}; border-radius:20px;
                    border: 1px solid {border_bg};
                ">{icon}</div>
                <div style="font-size:18px; font-weight:700; color:#121317; margin-bottom:10px;">{title}</div>
                <div style="font-size:14px; color:#5F6368; line-height:1.7;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:48px'></div>", unsafe_allow_html=True)

    # ===== HOW IT WORKS =====
    st.markdown('<div class="section-header">🔄 How It Works</div>', unsafe_allow_html=True)

    steps = [
        ("01", "Upload", "Upload your inventory & sales CSV files", "#3279F9"),
        ("02", "Process", "Auto-validate, clean, and transform data", "#7B61FF"),
        ("03", "Analyze", "KPIs, trends, and demand insights generated", "#1E8E3E"),
        ("04", "Optimize", "Act on data-driven recommendations", "#F9AB00"),
    ]

    cols = st.columns(4)
    for i, (col, (num, title, desc, color)) in enumerate(zip(cols, steps)):
        with col:
            st.markdown(f"""
            <div class="glass-card delay-{i+1}" style="text-align:center; min-height:180px;">
                <div style="
                    font-size:13px; font-weight:700; color: white;
                    margin-bottom:14px;
                    width:40px; height:40px;
                    display:inline-flex; align-items:center; justify-content:center;
                    background: {color}; border-radius: 9999px;
                    letter-spacing: 0.5px;
                ">{num}</div>
                <div style="font-size:17px; font-weight:700; color:#121317; margin-bottom:8px;">{title}</div>
                <div style="font-size:13px; color:#5F6368; line-height:1.65;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
