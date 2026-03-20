import streamlit as st

def set_layout():
    st.set_page_config(
        page_title="Stockify",
        page_icon="📦",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("""
    <style>
    /* ===== GOOGLE FONTS ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ===== ROOT VARIABLES ===== */
    :root {
        --bg-primary: #09090b;
        --bg-secondary: #0c0c10;
        --bg-card: rgba(255,255,255,0.03);
        --bg-card-hover: rgba(255,255,255,0.06);
        --bg-elevated: rgba(20, 20, 28, 0.9);
        --border-subtle: rgba(255,255,255,0.06);
        --border-hover: rgba(139, 92, 246, 0.4);
        --text-primary: #f4f4f5;
        --text-secondary: rgba(244,244,245,0.6);
        --text-muted: rgba(244,244,245,0.35);
        --accent-violet: #8b5cf6;
        --accent-cyan: #22d3ee;
        --accent-emerald: #34d399;
        --accent-amber: #fbbf24;
        --accent-rose: #fb7185;
        --accent-blue: #60a5fa;
        --glow-violet: rgba(139, 92, 246, 0.25);
        --glow-cyan: rgba(34, 211, 238, 0.2);
        --radius: 16px;
        --radius-sm: 12px;
        --transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ===== GLOBAL RESET ===== */
    *, *::before, *::after { box-sizing: border-box; }

    .stApp {
        background: var(--bg-primary) !important;
        color: var(--text-primary);
        font-family: 'Inter', -apple-system, sans-serif;
    }

    /* Subtle background noise/pattern */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background:
            radial-gradient(ellipse 80% 60% at 50% -20%, rgba(139,92,246,0.12), transparent),
            radial-gradient(ellipse 60% 50% at 80% 50%, rgba(34,211,238,0.06), transparent),
            radial-gradient(ellipse 50% 40% at 10% 80%, rgba(251,113,133,0.05), transparent);
        pointer-events: none;
        z-index: 0;
    }

    /* Hide default sidebar */
    section[data-testid="stSidebar"] { display: none !important; }
    button[data-testid="stSidebarCollapsedControl"] { display: none !important; }

    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: rgba(139,92,246,0.2);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover { background: rgba(139,92,246,0.4); }

    /* ===== KEYFRAME ANIMATIONS ===== */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(24px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.94); }
        to   { opacity: 1; transform: scale(1); }
    }
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-20px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 0 0 var(--glow-violet); }
        50%      { box-shadow: 0 0 24px 8px var(--glow-violet); }
    }
    @keyframes shimmer {
        0%   { background-position: -200% center; }
        100% { background-position: 200% center; }
    }
    @keyframes gradientText {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50%      { transform: translateY(-8px); }
    }
    @keyframes borderPulse {
        0%, 100% { border-color: rgba(139,92,246,0.15); }
        50%      { border-color: rgba(139,92,246,0.45); }
    }
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 8px rgba(139,92,246,0.15); }
        50%      { box-shadow: 0 0 24px rgba(139,92,246,0.3); }
    }
    @keyframes neonFlicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
            text-shadow: 0 0 10px rgba(139,92,246,0.6), 0 0 40px rgba(139,92,246,0.3);
        }
        20%, 24%, 55% {
            text-shadow: none;
        }
    }
    @keyframes rotateGradient {
        0%   { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* ===== TOP NAV BAR ===== */
    .top-nav {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        padding: 14px 24px;
        margin: -1rem -1rem 2rem -1rem;
        background: rgba(9, 9, 11, 0.92);
        backdrop-filter: blur(24px) saturate(150%);
        border-bottom: 1px solid var(--border-subtle);
        animation: fadeInUp 0.5s ease-out;
        position: sticky;
        top: 0;
        z-index: 999;
    }

    .nav-brand {
        font-size: 24px;
        font-weight: 900;
        background: linear-gradient(135deg, var(--accent-violet), var(--accent-cyan));
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientText 3s ease infinite;
        margin-right: 36px;
        letter-spacing: -0.5px;
    }

    /* ===== GLASSMORPHISM CARD ===== */
    .glass-card {
        background: var(--bg-card);
        backdrop-filter: blur(16px) saturate(120%);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius);
        padding: 28px;
        transition: var(--transition);
        animation: fadeInUp 0.6s ease-out backwards;
        position: relative;
        overflow: hidden;
    }
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(139,92,246,0.3), rgba(34,211,238,0.2), transparent);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    .glass-card:hover {
        transform: translateY(-6px);
        border-color: var(--border-hover);
        background: var(--bg-card-hover);
        box-shadow:
            0 20px 60px rgba(0,0,0,0.4),
            0 0 0 1px rgba(139,92,246,0.15),
            inset 0 1px 0 rgba(255,255,255,0.05);
    }
    .glass-card:hover::before { opacity: 1; }

    /* ===== METRIC CARD ===== */
    .metric-card {
        background: var(--bg-card);
        backdrop-filter: blur(16px);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius);
        padding: 28px 22px;
        text-align: center;
        transition: var(--transition);
        animation: fadeInUp 0.6s ease-out backwards;
        position: relative;
        overflow: hidden;
    }
    .metric-card::before {
        content: '';
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(139,92,246,0.06), transparent 30%);
        animation: rotateGradient 8s linear infinite;
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    .metric-card:hover::before { opacity: 1; }
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow:
            0 24px 64px rgba(0,0,0,0.5),
            0 0 0 1px rgba(139,92,246,0.2);
    }
    .metric-card .metric-icon {
        font-size: 36px;
        margin-bottom: 10px;
        display: inline-block;
        animation: float 3s ease-in-out infinite;
    }
    .metric-card .metric-value {
        font-size: 32px;
        font-weight: 800;
        margin: 6px 0;
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
    }
    .metric-card .metric-label {
        font-size: 11px;
        color: var(--text-muted);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        position: relative;
        z-index: 1;
    }

    /* Metric card color variants */
    .metric-blue { border-color: rgba(96,165,250,0.2); }
    .metric-blue .metric-value { color: var(--accent-blue); }
    .metric-blue:hover {
        border-color: rgba(96,165,250,0.5);
        box-shadow: 0 24px 64px rgba(0,0,0,0.5), 0 0 30px rgba(96,165,250,0.1);
    }

    .metric-green { border-color: rgba(52,211,153,0.2); }
    .metric-green .metric-value { color: var(--accent-emerald); }
    .metric-green:hover {
        border-color: rgba(52,211,153,0.5);
        box-shadow: 0 24px 64px rgba(0,0,0,0.5), 0 0 30px rgba(52,211,153,0.1);
    }

    .metric-purple { border-color: rgba(139,92,246,0.2); }
    .metric-purple .metric-value { color: var(--accent-violet); }
    .metric-purple:hover {
        border-color: rgba(139,92,246,0.5);
        box-shadow: 0 24px 64px rgba(0,0,0,0.5), 0 0 30px rgba(139,92,246,0.1);
    }

    .metric-orange { border-color: rgba(251,191,36,0.2); }
    .metric-orange .metric-value { color: var(--accent-amber); }
    .metric-orange:hover {
        border-color: rgba(251,191,36,0.5);
        box-shadow: 0 24px 64px rgba(0,0,0,0.5), 0 0 30px rgba(251,191,36,0.1);
    }

    .metric-red { border-color: rgba(251,113,133,0.2); }
    .metric-red .metric-value { color: var(--accent-rose); }
    .metric-red:hover {
        border-color: rgba(251,113,133,0.5);
        box-shadow: 0 24px 64px rgba(0,0,0,0.5), 0 0 30px rgba(251,113,133,0.1);
    }

    /* ===== HERO SECTION ===== */
    .hero-title {
        font-size: 56px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, var(--accent-violet), var(--accent-cyan), var(--accent-violet));
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientText 4s ease infinite, fadeInUp 0.8s ease-out;
        line-height: 1.1;
        margin-bottom: 10px;
        letter-spacing: -2px;
    }

    .hero-sub {
        text-align: center;
        color: var(--text-secondary);
        font-size: 18px;
        font-weight: 400;
        animation: fadeInUp 0.8s ease-out 0.15s backwards;
        margin-bottom: 36px;
        max-width: 550px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }

    /* ===== PAGE TITLES ===== */
    .page-title {
        font-size: 38px;
        font-weight: 900;
        background: linear-gradient(135deg, #c4b5fd, var(--accent-cyan));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: fadeInUp 0.5s ease-out;
        margin-bottom: 4px;
        letter-spacing: -1px;
    }
    .page-subtitle {
        color: var(--text-muted);
        font-size: 14px;
        animation: fadeInUp 0.5s ease-out 0.1s backwards;
        margin-bottom: 32px;
        font-weight: 400;
    }

    /* ===== SECTION HEADERS ===== */
    .section-header {
        font-size: 18px;
        font-weight: 700;
        color: var(--text-primary);
        margin: 32px 0 18px 0;
        padding-bottom: 10px;
        border-bottom: 1px solid var(--border-subtle);
        animation: fadeInUp 0.5s ease-out backwards;
        position: relative;
    }
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -1px;
        left: 0;
        width: 60px;
        height: 2px;
        background: linear-gradient(90deg, var(--accent-violet), var(--accent-cyan));
        border-radius: 2px;
    }

    /* ===== CHART CONTAINER ===== */
    .chart-container {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius);
        padding: 24px;
        animation: fadeInScale 0.6s ease-out backwards;
        transition: var(--transition);
    }
    .chart-container:hover {
        border-color: rgba(139,92,246,0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }

    /* ===== LOGIN CARD ===== */
    .login-card {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(24px) saturate(150%);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 24px;
        padding: 44px 40px;
        animation: fadeInScale 0.7s ease-out;
        box-shadow:
            0 32px 80px rgba(0,0,0,0.5),
            inset 0 1px 0 rgba(255,255,255,0.05);
        position: relative;
        overflow: hidden;
    }
    .login-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--accent-violet), var(--accent-cyan), var(--accent-violet));
        background-size: 200% 100%;
        animation: shimmer 3s ease-in-out infinite;
    }
    .login-title {
        font-size: 30px;
        font-weight: 800;
        color: var(--text-primary);
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }
    .login-sub {
        color: var(--text-muted);
        font-size: 14px;
        margin-bottom: 28px;
    }

    /* ===== FEATURE ITEMS ===== */
    .feature-item {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 16px 20px;
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-sm);
        margin-bottom: 10px;
        transition: var(--transition);
        animation: fadeInUp 0.6s ease-out backwards;
        cursor: default;
    }
    .feature-item:hover {
        background: rgba(139,92,246,0.06);
        border-color: rgba(139,92,246,0.25);
        transform: translateX(8px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    .feature-icon {
        font-size: 22px;
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(139,92,246,0.1);
        border: 1px solid rgba(139,92,246,0.15);
        border-radius: var(--radius-sm);
        flex-shrink: 0;
    }
    .feature-text {
        font-size: 14px;
        color: var(--text-secondary);
        font-weight: 500;
    }

    /* ===== UPLOAD ZONE ===== */
    .upload-zone {
        background: var(--bg-card);
        border: 2px dashed rgba(139,92,246,0.2);
        border-radius: var(--radius);
        padding: 28px;
        transition: var(--transition);
        animation: fadeInUp 0.6s ease-out backwards;
    }
    .upload-zone:hover {
        border-color: rgba(139,92,246,0.5);
        background: rgba(139,92,246,0.04);
        box-shadow: 0 0 40px rgba(139,92,246,0.08);
    }

    /* ===== RECOMMENDATION CARDS ===== */
    .rec-card {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-sm);
        padding: 20px 24px;
        margin-bottom: 12px;
        display: flex;
        align-items: flex-start;
        gap: 16px;
        transition: var(--transition);
        animation: fadeInUp 0.5s ease-out backwards;
        cursor: default;
    }
    .rec-card:hover {
        background: rgba(139,92,246,0.04);
        border-color: rgba(139,92,246,0.2);
        transform: translateX(6px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    }
    .rec-icon {
        font-size: 20px;
        flex-shrink: 0;
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: var(--radius-sm);
    }
    .rec-text {
        color: var(--text-secondary);
        font-size: 14px;
        line-height: 1.6;
    }
    .rec-text strong {
        color: var(--text-primary);
        font-weight: 600;
    }

    /* ===== DIVIDER ===== */
    hr {
        border: none;
        border-top: 1px solid var(--border-subtle);
        margin: 28px 0;
    }

    /* ===== STREAMLIT BUTTON OVERRIDES ===== */
    .stButton > button {
        background: linear-gradient(135deg, var(--accent-violet), #7c3aed) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        padding: 12px 30px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        font-family: 'Inter', sans-serif !important;
        transition: var(--transition) !important;
        letter-spacing: 0.3px;
        position: relative;
        overflow: hidden;
    }
    .stButton > button::after {
        content: '';
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: linear-gradient(
            transparent,
            rgba(255,255,255,0.05),
            transparent
        );
        transform: rotate(45deg);
        transition: all 0.5s ease;
        opacity: 0;
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.03) !important;
        box-shadow: 0 12px 36px rgba(139,92,246,0.35), 0 0 0 1px rgba(139,92,246,0.3) !important;
        background: linear-gradient(135deg, #9b7bf7, var(--accent-violet)) !important;
    }
    .stButton > button:hover::after { opacity: 1; }
    .stButton > button:active {
        transform: scale(0.97) !important;
    }

    /* Input fields */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: var(--radius-sm) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
        padding: 14px 18px !important;
        transition: var(--transition) !important;
        font-size: 14px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: rgba(139,92,246,0.5) !important;
        box-shadow: 0 0 0 3px rgba(139,92,246,0.1), 0 0 20px rgba(139,92,246,0.1) !important;
        background: rgba(255,255,255,0.06) !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: var(--text-muted) !important;
    }

    /* Labels */
    .stTextInput label, .stFileUploader label, .stSelectbox label {
        color: var(--text-secondary) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        font-size: 13px !important;
    }

    /* Dataframe */
    .stDataFrame {
        animation: fadeInUp 0.6s ease-out backwards;
        border-radius: var(--radius) !important;
        overflow: hidden;
    }

    /* Metric overrides */
    [data-testid="stMetric"] {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-sm);
        padding: 18px;
        transition: var(--transition);
    }
    [data-testid="stMetric"]:hover {
        border-color: rgba(139,92,246,0.3);
        transform: translateY(-3px);
        box-shadow: 0 12px 32px rgba(0,0,0,0.3);
    }
    [data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 11px !important;
    }
    [data-testid="stMetricValue"] {
        color: var(--text-primary) !important;
        font-weight: 800 !important;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background: var(--bg-card);
        border: 2px dashed rgba(139,92,246,0.15);
        border-radius: var(--radius);
        padding: 24px;
        transition: var(--transition);
    }
    [data-testid="stFileUploader"]:hover {
        border-color: rgba(139,92,246,0.4);
        background: rgba(139,92,246,0.03);
        box-shadow: 0 0 30px rgba(139,92,246,0.06);
    }

    /* Tables */
    .stTable {
        animation: fadeInUp 0.6s ease-out backwards;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: var(--bg-card) !important;
        border-radius: var(--radius-sm) !important;
        color: var(--text-primary) !important;
        font-weight: 600;
        transition: var(--transition);
        border: 1px solid var(--border-subtle);
    }
    .streamlit-expanderHeader:hover {
        background: rgba(139,92,246,0.06) !important;
        border-color: rgba(139,92,246,0.2);
    }

    /* Alerts */
    .stAlert {
        border-radius: var(--radius-sm) !important;
        animation: fadeInUp 0.4s ease-out;
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 4px; }
    .stTabs [data-baseweb="tab"] {
        background: var(--bg-card);
        border-radius: 10px;
        color: var(--text-secondary);
        border: 1px solid transparent;
        transition: var(--transition);
    }
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(139,92,246,0.08);
        color: var(--text-primary);
    }
    .stTabs [aria-selected="true"] {
        background: rgba(139,92,246,0.12) !important;
        color: #c4b5fd !important;
        border-color: rgba(139,92,246,0.25) !important;
    }

    /* Hide streamlit branding */
    #MainMenu { visibility: hidden; }
    header { visibility: hidden; }
    footer { visibility: hidden; }

    /* ===== STAT BADGE ===== */
    .stat-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.3px;
    }
    .stat-badge-green {
        background: rgba(52,211,153,0.1);
        color: var(--accent-emerald);
        border: 1px solid rgba(52,211,153,0.2);
    }
    .stat-badge-red {
        background: rgba(251,113,133,0.1);
        color: var(--accent-rose);
        border: 1px solid rgba(251,113,133,0.2);
    }

    /* ===== ANIMATION DELAYS ===== */
    .delay-1 { animation-delay: 0.1s !important; }
    .delay-2 { animation-delay: 0.2s !important; }
    .delay-3 { animation-delay: 0.3s !important; }
    .delay-4 { animation-delay: 0.4s !important; }
    .delay-5 { animation-delay: 0.5s !important; }
    .delay-6 { animation-delay: 0.6s !important; }

    /* ===== GLOW HIGHLIGHT ===== */
    .glow-box {
        position: relative;
    }
    .glow-box::after {
        content: '';
        position: absolute;
        inset: -1px;
        border-radius: var(--radius);
        background: linear-gradient(135deg, var(--accent-violet), var(--accent-cyan), var(--accent-violet));
        z-index: -1;
        opacity: 0;
        transition: opacity 0.4s ease;
        filter: blur(12px);
    }
    .glow-box:hover::after { opacity: 0.15; }

    </style>
    """, unsafe_allow_html=True)
