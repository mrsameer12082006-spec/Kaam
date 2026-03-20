import streamlit as st
import pandas as pd

def show_trends():
    results = st.session_state.get("analytics_results", {})

    st.markdown('<div class="page-title">📈 Trends Analysis</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Track revenue patterns, category performance, and product movements over time</div>',
        unsafe_allow_html=True,
    )

    daily_trends = results.get("daily_trends", pd.DataFrame())

    if not daily_trends.empty:
        time_period = f"{daily_trends['date'].min()} → {daily_trends['date'].max()}"
        revenue_trend = (
            daily_trends["revenue"].pct_change().mean() * 100
            if len(daily_trends) > 1
            else 0
        )
        daily_avg = daily_trends["revenue"].mean()
    else:
        time_period = "—"
        revenue_trend = 0
        daily_avg = 0

    # ===== METRIC CARDS =====
    col1, col2, col3 = st.columns(3)

    trend_metrics = [
        ("📅", "Time Period", time_period, "metric-blue", col1),
        ("📈", "Revenue Trend", f"{revenue_trend:+.1f}%", "metric-green", col2),
        ("💵", "Daily Average", f"${daily_avg:.2f}", "metric-purple", col3),
    ]

    for i, (icon, label, value, color_class, col) in enumerate(trend_metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card {color_class} delay-{i+1}">
                <div class="metric-icon">{icon}</div>
                <div class="metric-value" style="font-size:22px;">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)

    # ===== REVENUE TREND CHART =====
    st.markdown('<div class="section-header">📈 Revenue & Quantity Trend</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-container delay-2">', unsafe_allow_html=True)
    if not daily_trends.empty:
        st.line_chart(daily_trends.set_index("date")[["revenue", "quantity"]])
    else:
        st.markdown("""
        <div style="text-align:center; padding:40px 20px; color:rgba(244,244,245,0.3);">
            <div style="font-size:36px; margin-bottom:8px;">📭</div>
            <div style="font-size:13px;">Upload sales data to see trends</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

    # ===== CATEGORY CHART =====
    st.markdown('<div class="section-header">📊 Category Performance</div>', unsafe_allow_html=True)
    category_demand = results.get("category_demand", pd.DataFrame())
    st.markdown('<div class="chart-container delay-3">', unsafe_allow_html=True)
    if not category_demand.empty:
        st.bar_chart(category_demand.set_index("category")[["revenue", "quantity"]])
    else:
        st.markdown("""
        <div style="text-align:center; padding:40px 20px; color:rgba(244,244,245,0.3);">
            <div style="font-size:36px; margin-bottom:8px;">📭</div>
            <div style="font-size:13px;">Upload data to see category trends</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

    # ===== TOP PRODUCTS =====
    st.markdown('<div class="section-header">🏆 Top Products Trend</div>', unsafe_allow_html=True)
    top_products = results.get("top_products", pd.DataFrame())
    st.markdown('<div class="chart-container delay-4">', unsafe_allow_html=True)
    if not top_products.empty:
        st.dataframe(top_products, use_container_width=True)
    else:
        st.markdown("""
        <div style="text-align:center; padding:40px 20px; color:rgba(244,244,245,0.3);">
            <div style="font-size:36px; margin-bottom:8px;">📭</div>
            <div style="font-size:13px;">Upload data to see product trends</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
