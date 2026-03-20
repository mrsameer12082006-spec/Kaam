import streamlit as st
import pandas as pd

def show_insights():
    results = st.session_state.get("analytics_results", {})

    st.markdown('<div class="page-title">💡 Insights & Recommendations</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Data-driven intelligence to optimize your inventory strategy</div>',
        unsafe_allow_html=True,
    )

    product_demand = results.get("product_demand", pd.DataFrame())
    kpis = results.get("kpis", {})

    # Classify demand
    if not product_demand.empty:
        avg_quantity = product_demand["totalQuantity"].mean()
        high_demand = len(product_demand[product_demand["totalQuantity"] > avg_quantity * 1.5])
        medium_demand = len(
            product_demand[
                (product_demand["totalQuantity"] <= avg_quantity * 1.5)
                & (product_demand["totalQuantity"] >= avg_quantity * 0.5)
            ]
        )
        low_demand = len(product_demand[product_demand["totalQuantity"] < avg_quantity * 0.5])
        critical = kpis.get("slow_moving_count", 0)
    else:
        high_demand = 0
        medium_demand = 0
        low_demand = 0
        critical = 0

    # ===== DEMAND CARDS =====
    col1, col2, col3, col4 = st.columns(4)

    insight_cards = [
        ("🔥", "High Demand", str(high_demand), "metric-green", col1),
        ("⚡", "Medium Demand", str(medium_demand), "metric-blue", col2),
        ("❄️", "Low Demand", str(low_demand), "metric-orange", col3),
        ("🚨", "Critical", str(critical), "metric-red", col4),
    ]

    for i, (icon, label, value, color_class, col) in enumerate(insight_cards):
        with col:
            st.markdown(f"""
            <div class="metric-card {color_class} delay-{i+1}">
                <div class="metric-icon">{icon}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)

    # ===== RECOMMENDATIONS =====
    st.markdown('<div class="section-header">🎯 Smart Recommendations</div>', unsafe_allow_html=True)

    if not product_demand.empty:
        top_product = kpis.get("top_selling_product", "")

        # Top seller card
        st.markdown(f"""
        <div class="glass-card delay-2" style="margin-bottom:24px; position:relative; overflow:hidden;">
            <div style="position:absolute; top:0; right:0; width:200px; height:200px;
                        background:radial-gradient(circle, rgba(30,142,62,0.06), transparent 70%);
                        pointer-events:none;"></div>
            <div style="display:flex; align-items:center; gap:18px; position:relative; z-index:1;">
                <div style="
                    font-size:40px;
                    width:68px; height:68px;
                    display:flex; align-items:center; justify-content:center;
                    background:rgba(30,142,62,0.08);
                    border:1px solid rgba(30,142,62,0.15);
                    border-radius:18px;
                ">🏆</div>
                <div>
                    <div style="font-size:11px; color:#9AA0A6; text-transform:uppercase;
                                letter-spacing:1.5px; font-weight:700;">Top Selling Product</div>
                    <div style="font-size:26px; font-weight:700; color:#1E8E3E; margin-top:4px;
                                letter-spacing:-0.5px;">{top_product}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Recommendation cards
        recommendations = [
            ("📦", "rgba(30,142,62,0.08)", "rgba(30,142,62,0.12)", "Stock Up on Winners",
             "Allocate more shelf space and maintain higher stock levels for your best-selling items to maximize revenue potential."),
            ("🏷️", "rgba(249,171,0,0.08)", "rgba(249,171,0,0.12)", "Clear Slow Movers",
             "Bundle deals, flash sales, or seasonal promotions can help move aging inventory and recover tied-up capital."),
            ("🔍", "rgba(217,48,37,0.08)", "rgba(217,48,37,0.12)", "Watch Critical Items",
             "Set up automated alerts for products approaching reorder points to prevent costly stockouts."),
            ("📊", "rgba(50,121,249,0.08)", "rgba(50,121,249,0.12)", "Weekly Category Review",
             "Review category performance every week to spot emerging demand shifts and adjust purchasing ahead of trends."),
        ]

        for i, (icon, bg, border_bg, title, desc) in enumerate(recommendations):
            st.markdown(f"""
            <div class="rec-card delay-{i+3}">
                <div class="rec-icon" style="background:{bg}; border:1px solid {border_bg};">{icon}</div>
                <div class="rec-text">
                    <strong>{title}</strong><br>
                    {desc}
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="glass-card" style="text-align:center; padding:52px 20px;">
            <div style="font-size:52px; margin-bottom:14px; filter:drop-shadow(0 0 16px rgba(50,121,249,0.15));">📭</div>
            <div style="font-size:18px; font-weight:700; color:#121317; margin-bottom:6px;">No Data Available</div>
            <div style="font-size:13px; color:#9AA0A6; max-width:360px; margin:0 auto;">
                Upload inventory and sales data to unlock personalized AI-powered recommendations.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)

    # ===== BEST PRACTICES =====
    st.markdown('<div class="section-header">📚 Best Practices</div>', unsafe_allow_html=True)

    tips = [
        ("✅", "Maintain inventory levels above reorder points to prevent costly stockouts"),
        ("📈", "Analyze sales trends at least weekly — catch demand shifts before competitors do"),
        ("🧮", "Replace gut-feel ordering with data-driven quantity calculations"),
        ("🔄", "Reassess reorder points quarterly as customer demand patterns evolve"),
        ("📋", "Standardize CSV formatting across your team for consistent analytics"),
    ]

    for i, (icon, tip) in enumerate(tips):
        st.markdown(f"""
        <div class="rec-card delay-{i+1}">
            <div class="rec-icon" style="background:rgba(50,121,249,0.06); border:1px solid rgba(50,121,249,0.1);">{icon}</div>
            <div class="rec-text">{tip}</div>
        </div>
        """, unsafe_allow_html=True)
