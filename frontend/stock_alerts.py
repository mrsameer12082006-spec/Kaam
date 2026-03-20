import streamlit as st
import pandas as pd


def show_stock_alerts():
    results = st.session_state.get("analytics_results", {})

    st.markdown('<div class="page-title">🚨 Stock Health & Alerts</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Automated inventory risk assessment with reorder recommendations</div>',
        unsafe_allow_html=True,
    )

    stock_recs = results.get("stock_recommendations", pd.DataFrame())

    if not stock_recs.empty:
        # ===== SUMMARY CARDS =====
        low_stock = len(stock_recs[stock_recs["Alert Type"] == "Low Stock"])
        healthy = len(stock_recs[stock_recs["Alert Type"] == "Healthy"])
        overstock = len(stock_recs[stock_recs["Alert Type"] == "Overstock"])
        high_risk = len(stock_recs[stock_recs["Risk Level"] == "High"])

        col1, col2, col3, col4 = st.columns(4)

        alert_cards = [
            ("🔻", "Low Stock", str(low_stock), "metric-red", col1),
            ("✅", "Healthy", str(healthy), "metric-green", col2),
            ("📦", "Overstock", str(overstock), "metric-orange", col3),
            ("⚠️", "High Risk", str(high_risk), "metric-purple", col4),
        ]

        for i, (icon, label, value, color_class, col) in enumerate(alert_cards):
            with col:
                st.markdown(f"""
                <div class="metric-card {color_class} delay-{i+1}">
                    <div class="metric-icon">{icon}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)

        # ===== RISK DISTRIBUTION =====
        st.markdown('<div class="section-header">📊 Risk Distribution</div>', unsafe_allow_html=True)

        risk_counts = stock_recs["Risk Level"].value_counts()
        risk_col1, risk_col2, risk_col3 = st.columns(3)

        risk_colors = {"High": "#D93025", "Medium": "#F9AB00", "Low": "#1E8E3E"}
        risk_icons = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}

        for i, (col, level) in enumerate(zip([risk_col1, risk_col2, risk_col3], ["High", "Medium", "Low"])):
            count = risk_counts.get(level, 0)
            total = len(stock_recs)
            pct = round((count / total) * 100, 1) if total > 0 else 0
            color = risk_colors[level]
            icon = risk_icons[level]

            with col:
                st.markdown(f"""
                <div class="glass-card delay-{i+2}" style="text-align:center; padding:28px 20px;">
                    <div style="font-size:32px; margin-bottom:8px;">{icon}</div>
                    <div style="font-size:28px; font-weight:700; color:{color}; letter-spacing:-0.5px;">{count}</div>
                    <div style="font-size:12px; color:#9AA0A6; margin-top:4px; text-transform:uppercase;
                                letter-spacing:1px; font-weight:600;">{level} Risk</div>
                    <div style="margin-top:12px; background:rgba(0,0,0,0.04); border-radius:8px;
                                height:6px; overflow:hidden;">
                        <div style="width:{pct}%; height:100%; background:{color}; border-radius:8px;
                                    transition: width 0.6s ease;"></div>
                    </div>
                    <div style="font-size:11px; color:#9AA0A6; margin-top:6px;">{pct}% of products</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)

        # ===== ALERTS TABLE =====
        st.markdown('<div class="section-header">📋 Detailed Stock Alerts</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-container delay-3">', unsafe_allow_html=True)

        # Color-code the alert types
        def style_alert_type(val):
            colors = {
                "Low Stock": "background-color: rgba(217,48,37,0.08); color: #D93025; font-weight:600;",
                "Overstock": "background-color: rgba(249,171,0,0.08); color: #F9AB00; font-weight:600;",
                "Healthy": "background-color: rgba(30,142,62,0.08); color: #1E8E3E; font-weight:600;",
            }
            return colors.get(val, "")

        def style_risk(val):
            colors = {
                "High": "background-color: rgba(217,48,37,0.08); color: #D93025; font-weight:600;",
                "Medium": "background-color: rgba(249,171,0,0.08); color: #F9AB00; font-weight:600;",
                "Low": "background-color: rgba(30,142,62,0.08); color: #1E8E3E; font-weight:600;",
            }
            return colors.get(val, "")

        display_cols = [
            "Product Name", "Current Stock", "Reorder Point", "Alert Type",
            "Risk Level", "Stock Value", "Profit Margin (%)",
            "Suggested Reorder Quantity", "Recommendation"
        ]

        available_cols = [c for c in display_cols if c in stock_recs.columns]
        display_df = stock_recs[available_cols].copy()

        styled = display_df.style
        if "Alert Type" in available_cols:
            styled = styled.map(style_alert_type, subset=["Alert Type"])
        if "Risk Level" in available_cols:
            styled = styled.map(style_risk, subset=["Risk Level"])

        st.dataframe(styled, use_container_width=True, height=400)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)

        # ===== PRODUCTS NEEDING REORDER =====
        needs_reorder = stock_recs[stock_recs["Suggested Reorder Quantity"] > 0] if "Suggested Reorder Quantity" in stock_recs.columns else pd.DataFrame()

        if not needs_reorder.empty:
            st.markdown('<div class="section-header">🔄 Products Needing Reorder</div>', unsafe_allow_html=True)

            for i, (_, row) in enumerate(needs_reorder.iterrows()):
                urgency_color = "#D93025" if row.get("Risk Level") == "High" else "#F9AB00"
                urgency_label = "URGENT" if row.get("Risk Level") == "High" else "RECOMMENDED"

                st.markdown(f"""
                <div class="rec-card delay-{min(i+1, 5)}">
                    <div class="rec-icon" style="background:rgba(50,121,249,0.06); border:1px solid rgba(50,121,249,0.1);">
                        📦
                    </div>
                    <div class="rec-text" style="flex:1;">
                        <strong>{row['Product Name']}</strong><br>
                        <span style="font-size:12px;">
                            Current: <strong>{row['Current Stock']}</strong> units
                            &nbsp;•&nbsp; Reorder Point: <strong>{row['Reorder Point']}</strong>
                            &nbsp;•&nbsp; Suggested Order: <strong style="color:#3279F9;">{row['Suggested Reorder Quantity']}</strong> units
                        </span>
                    </div>
                    <div style="padding:4px 12px; border-radius:9999px; font-size:10px; font-weight:700;
                                letter-spacing:0.5px; background:rgba({217 if urgency_label=='URGENT' else 249},{48 if urgency_label=='URGENT' else 171},{37 if urgency_label=='URGENT' else 0},0.08);
                                color:{urgency_color};">{urgency_label}</div>
                </div>
                """, unsafe_allow_html=True)
    else:
        # Empty state
        st.markdown("""
        <div class="glass-card" style="text-align:center; padding:56px 20px;">
            <div style="font-size:56px; margin-bottom:16px; filter:drop-shadow(0 0 16px rgba(50,121,249,0.15));">🚨</div>
            <div style="font-size:20px; font-weight:700; color:#121317; margin-bottom:8px;">No Inventory Data</div>
            <div style="font-size:14px; color:#9AA0A6; max-width:400px; margin:0 auto;">
                Upload your inventory CSV file to unlock automated stock health alerts,
                risk assessment, and smart reorder recommendations.
            </div>
        </div>
        """, unsafe_allow_html=True)
