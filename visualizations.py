import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Ensure project root is importable
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


def show_visualizations():
    results = st.session_state.get("analytics_results", {})

    st.markdown('<div class="page-title">📉 Advanced Charts</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Interactive visualizations powered by your inventory and sales data</div>',
        unsafe_allow_html=True,
    )

    product_demand = results.get("product_demand", pd.DataFrame())
    daily_trends = results.get("daily_trends", pd.DataFrame())
    kpis = results.get("kpis", {})
    stock_recs = results.get("stock_recommendations", pd.DataFrame())

    has_data = not product_demand.empty or not daily_trends.empty

    if has_data:
        # ===== KPI OVERVIEW STRIP =====
        st.markdown('<div class="section-header">📊 Key Performance Indicators</div>', unsafe_allow_html=True)

        kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
        kpi_items = [
            ("🏷️", "Total Products", str(kpis.get("total_products", 0)), "metric-blue", kpi_col1),
            ("📦", "Units Sold", f"{kpis.get('total_sales_quantity', 0):,}", "metric-green", kpi_col2),
            ("🏆", "Top Product", kpis.get("top_selling_product", "N/A"), "metric-purple", kpi_col3),
            ("🐌", "Slow Movers", str(kpis.get("slow_moving_count", 0)), "metric-orange", kpi_col4),
        ]

        for i, (icon, label, value, color_class, col) in enumerate(kpi_items):
            with col:
                st.markdown(f"""
                <div class="metric-card {color_class} delay-{i+1}">
                    <div class="metric-icon">{icon}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)

        # ===== PRODUCT DEMAND BAR CHART =====
        if not product_demand.empty:
            st.markdown('<div class="section-header">📦 Product Demand Comparison</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-container delay-2">', unsafe_allow_html=True)

            # Sort by quantity descending, top 15
            chart_data = product_demand.nlargest(15, "totalQuantity")

            if "product" in chart_data.columns:
                chart_df = chart_data.set_index("product")[["totalQuantity"]].rename(
                    columns={"totalQuantity": "Units Sold"}
                )
            elif "product_name" in chart_data.columns:
                chart_df = chart_data.set_index("product_name")[["totalQuantity"]].rename(
                    columns={"totalQuantity": "Units Sold"}
                )
            else:
                chart_df = chart_data[["totalQuantity"]].rename(
                    columns={"totalQuantity": "Units Sold"}
                )

            st.bar_chart(chart_df, color="#3279F9")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)

        # ===== SALES TREND LINE CHART =====
        if not daily_trends.empty:
            st.markdown('<div class="section-header">📈 Sales Trend Over Time</div>', unsafe_allow_html=True)

            trend_col1, trend_col2 = st.columns(2)

            with trend_col1:
                st.markdown('<div class="chart-container delay-3">', unsafe_allow_html=True)
                st.markdown("""
                <div style="font-size:13px; font-weight:600; color:#5F6368; margin-bottom:12px;">
                    Revenue Trend
                </div>
                """, unsafe_allow_html=True)
                if "revenue" in daily_trends.columns:
                    st.line_chart(daily_trends.set_index("date")["revenue"], color="#3279F9")
                st.markdown('</div>', unsafe_allow_html=True)

            with trend_col2:
                st.markdown('<div class="chart-container delay-4">', unsafe_allow_html=True)
                st.markdown("""
                <div style="font-size:13px; font-weight:600; color:#5F6368; margin-bottom:12px;">
                    Units Sold Trend
                </div>
                """, unsafe_allow_html=True)
                if "quantity" in daily_trends.columns:
                    st.line_chart(daily_trends.set_index("date")["quantity"], color="#1E8E3E")
                st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)

        # ===== REVENUE BY CATEGORY =====
        category_demand = results.get("category_demand", pd.DataFrame())
        if not category_demand.empty:
            st.markdown('<div class="section-header">🏪 Revenue by Category</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-container delay-5">', unsafe_allow_html=True)

            if "category" in category_demand.columns and "revenue" in category_demand.columns:
                cat_chart = category_demand.set_index("category")[["revenue"]].rename(
                    columns={"revenue": "Revenue ($)"}
                )
                st.bar_chart(cat_chart, color="#7B61FF")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)

        # ===== INVENTORY ALERTS OVERVIEW =====
        if not stock_recs.empty:
            st.markdown('<div class="section-header">⚠️ Inventory Alerts</div>', unsafe_allow_html=True)

            alert_types = stock_recs["Alert Type"].value_counts() if "Alert Type" in stock_recs.columns else pd.Series()
            alert_icons = {"Low Stock": "🔻", "Overstock": "📦", "Healthy": "✅"}
            alert_colors = {"Low Stock": "#D93025", "Overstock": "#F9AB00", "Healthy": "#1E8E3E"}

            for alert_type, count in alert_types.items():
                products = stock_recs[stock_recs["Alert Type"] == alert_type]["Product Name"].tolist()
                icon = alert_icons.get(alert_type, "•")
                color = alert_colors.get(alert_type, "#5F6368")
                product_list = ", ".join(products[:5])
                if len(products) > 5:
                    product_list += f" (+{len(products)-5} more)"

                st.markdown(f"""
                <div class="rec-card delay-2">
                    <div class="rec-icon" style="background:rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.06);
                                border:1px solid rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.12);">
                        {icon}
                    </div>
                    <div class="rec-text" style="flex:1;">
                        <strong style="color:{color};">{alert_type}</strong>
                        <span style="margin-left:8px; padding:2px 10px; border-radius:9999px; font-size:11px;
                                    font-weight:700; background:rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.08);
                                    color:{color};">{count} products</span><br>
                        <span style="font-size:12px; color:#9AA0A6;">{product_list}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        # Empty state
        st.markdown("""
        <div class="glass-card" style="text-align:center; padding:56px 20px;">
            <div style="font-size:56px; margin-bottom:16px; filter:drop-shadow(0 0 16px rgba(50,121,249,0.15));">📉</div>
            <div style="font-size:20px; font-weight:700; color:#121317; margin-bottom:8px;">No Data to Visualize</div>
            <div style="font-size:14px; color:#9AA0A6; max-width:400px; margin:0 auto;">
                Upload inventory and sales CSV files to unlock interactive charts,
                trend analysis, and category breakdowns.
            </div>
        </div>
        """, unsafe_allow_html=True)
