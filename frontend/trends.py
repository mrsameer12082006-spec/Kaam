import streamlit as st
import pandas as pd

def show_trends():
    results = st.session_state.get("analytics_results", {})

    st.title("Trends")

    daily_trends = results.get("daily_trends", pd.DataFrame())

    if not daily_trends.empty:
        time_period = f"{daily_trends['date'].min()} to {daily_trends['date'].max()}"
        revenue_trend = daily_trends["revenue"].pct_change().mean() * 100 if len(daily_trends) > 1 else 0
        daily_avg = daily_trends["revenue"].mean()
    else:
        time_period = "—"
        revenue_trend = 0
        daily_avg = 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Time Period", time_period)
    col2.metric("Revenue Trend", f"{revenue_trend:+.1f}%")
    col3.metric("Daily Average", f"${daily_avg:.2f}")

    st.divider()

    st.subheader("Revenue Trend Graph")
    if not daily_trends.empty:
        st.line_chart(daily_trends.set_index("date")[["revenue", "quantity"]])
    else:
        st.write("No data available")

    st.subheader("Category Trend Graph")
    category_demand = results.get("category_demand", pd.DataFrame())
    if not category_demand.empty:
        st.bar_chart(category_demand.set_index("category")[["revenue", "quantity"]])
    else:
        st.write("No data available")

    st.subheader("Top Products Trend")
    top_products = results.get("top_products", pd.DataFrame())
    if not top_products.empty:
        st.dataframe(top_products)
    else:
        st.write("No data available")
