import streamlit as st

def show_home():
    # Hero Section
    st.markdown("""
    <div style="text-align:center; margin-bottom:8px; animation: float 4s ease-in-out infinite;">
        <span style="font-size:56px; filter: drop-shadow(0 0 24px rgba(139,92,246,0.4));">📦</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-title">Smart Inventory Decisions<br>for Small Retailers</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-sub">
        Stop relying on guesswork. Harness the power of data to optimize stock levels,<br>
        maximize revenue, and eliminate waste.
    </div>
    """, unsafe_allow_html=True)

    # CTA Button
    col1, col2, col3 = st.columns([1.5, 1, 1.5])
    with col2:
        st.markdown("""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button {
            animation: pulse 2.5s ease-in-out infinite !important;
            font-size: 16px !important;
            padding: 16px 36px !important;
            border-radius: 14px !important;
            background: linear-gradient(135deg, #8b5cf6, #22d3ee) !important;
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button:hover {
            background: linear-gradient(135deg, #a78bfa, #34d399) !important;
        }
        </style>
        """, unsafe_allow_html=True)
        if st.button("🚀 Start Analyzing", use_container_width=True):
            st.session_state.current_page = "📂 Upload"
            st.rerun()

    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

    # ===== STATS BAR =====
    st.markdown("""
    <div style="
        display: flex;
        justify-content: center;
        gap: 40px;
        padding: 20px;
        animation: fadeInUp 0.7s ease-out 0.3s backwards;
        margin-bottom: 48px;
    ">
        <div style="text-align:center;">
            <div style="font-size:28px; font-weight:800; color:#8b5cf6;">10x</div>
            <div style="font-size:12px; color:rgba(244,244,245,0.35); text-transform:uppercase; letter-spacing:1px; font-weight:600;">Faster Insights</div>
        </div>
        <div style="width:1px; background:rgba(255,255,255,0.06);"></div>
        <div style="text-align:center;">
            <div style="font-size:28px; font-weight:800; color:#22d3ee;">30%</div>
            <div style="font-size:12px; color:rgba(244,244,245,0.35); text-transform:uppercase; letter-spacing:1px; font-weight:600;">Less Waste</div>
        </div>
        <div style="width:1px; background:rgba(255,255,255,0.06);"></div>
        <div style="text-align:center;">
            <div style="font-size:28px; font-weight:800; color:#34d399;">2x</div>
            <div style="font-size:12px; color:rgba(244,244,245,0.35); text-transform:uppercase; letter-spacing:1px; font-weight:600;">Profit Growth</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===== THE PROBLEM =====
    st.markdown('<div class="section-header">😰 The Problem</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    problems = [
        ("📦", "Overstocking", "Excess inventory ties up capital and increases waste, eating into your margins.", "rgba(251,113,133,0.08)", "rgba(251,113,133,0.15)"),
        ("🚫", "Stock Shortages", "Running out of key items means lost sales and frustrated customers who won't return.", "rgba(251,191,36,0.08)", "rgba(251,191,36,0.15)"),
        ("📉", "Reduced Profit", "Without data, pricing and ordering decisions consistently leave money on the table.", "rgba(96,165,250,0.08)", "rgba(96,165,250,0.15)"),
    ]

    for i, (col, (icon, title, desc, bg, border_bg)) in enumerate(zip([col1, col2, col3], problems)):
        with col:
            st.markdown(f"""
            <div class="glass-card delay-{i+1}" style="text-align:center; min-height:200px;">
                <div style="
                    font-size:44px; margin-bottom:14px;
                    width:72px; height:72px;
                    display:inline-flex; align-items:center; justify-content:center;
                    background:{bg}; border-radius:20px;
                    border: 1px solid {border_bg};
                ">{icon}</div>
                <div style="font-size:18px; font-weight:700; color:#f4f4f5; margin-bottom:10px;">{title}</div>
                <div style="font-size:13px; color:rgba(244,244,245,0.45); line-height:1.7;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:44px'></div>", unsafe_allow_html=True)

    # ===== OUR SOLUTION =====
    st.markdown('<div class="section-header">✨ Our Solution</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    solutions = [
        ("📤", "Easy Upload", "Simply drag & drop your CSV files — inventory and sales data processed in seconds.", "rgba(139,92,246,0.08)", "rgba(139,92,246,0.15)"),
        ("⚡", "Instant Analysis", "Powerful analytics engine calculates KPIs, trends, and demand patterns automatically.", "rgba(34,211,238,0.08)", "rgba(34,211,238,0.15)"),
        ("🎯", "Visual Insights", "Beautiful charts and actionable recommendations to guide your next business move.", "rgba(52,211,153,0.08)", "rgba(52,211,153,0.15)"),
    ]

    for i, (col, (icon, title, desc, bg, border_bg)) in enumerate(zip([col1, col2, col3], solutions)):
        with col:
            st.markdown(f"""
            <div class="glass-card delay-{i+3}" style="text-align:center; min-height:200px;">
                <div style="
                    font-size:44px; margin-bottom:14px;
                    width:72px; height:72px;
                    display:inline-flex; align-items:center; justify-content:center;
                    background:{bg}; border-radius:20px;
                    border: 1px solid {border_bg};
                ">{icon}</div>
                <div style="font-size:18px; font-weight:700; color:#f4f4f5; margin-bottom:10px;">{title}</div>
                <div style="font-size:13px; color:rgba(244,244,245,0.45); line-height:1.7;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:44px'></div>", unsafe_allow_html=True)

    # ===== HOW IT WORKS =====
    st.markdown('<div class="section-header">🔄 How It Works</div>', unsafe_allow_html=True)

    steps = [
        ("01", "Upload", "Upload your inventory & sales CSV files", "#8b5cf6"),
        ("02", "Process", "Auto-validate, clean, and transform data", "#22d3ee"),
        ("03", "Analyze", "KPIs, trends, and demand insights generated", "#34d399"),
        ("04", "Optimize", "Act on data-driven recommendations", "#fbbf24"),
    ]

    cols = st.columns(4)
    for i, (col, (num, title, desc, color)) in enumerate(zip(cols, steps)):
        with col:
            st.markdown(f"""
            <div class="glass-card delay-{i+1}" style="text-align:center; min-height:170px;">
                <div style="
                    font-size:24px; font-weight:900; color:{color};
                    margin-bottom:10px; font-family:'JetBrains Mono', monospace;
                    opacity:0.8;
                ">{num}</div>
                <div style="font-size:16px; font-weight:700; color:#f4f4f5; margin-bottom:8px;">{title}</div>
                <div style="font-size:12px; color:rgba(244,244,245,0.4); line-height:1.6;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
