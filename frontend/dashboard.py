import streamlit as st
import pandas as pd

def show_dashboard():
    results = st.session_state.get("analytics_results", {})

    st.title("Overview")

    kpis = results.get("kpis", {})
    daily_trends = results.get("daily_trends", pd.DataFrame())
    category_demand = results.get("category_demand", pd.DataFrame())
    top_products = results.get("top_products", pd.DataFrame())

    # Metrics
    col1, col2, col3, col4 = st.columns(4)

    total_revenue = daily_trends["revenue"].sum() if not daily_trends.empty else 0
    total_quantity = kpis.get("total_sales_quantity", 0)
    total_products = kpis.get("total_products", 0)
    avg_transaction = total_revenue / max(daily_trends["transactions"].sum() if not daily_trends.empty else 1, 1)

    col1.metric("Total Revenue", f"${total_revenue:,.2f}")
    col2.metric("Units Sold", f"{total_quantity:,}")
    col3.metric("Products", f"{total_products:,}")
    col4.metric("Avg Transaction", f"${avg_transaction:.2f}")

    st.divider()

    colA, colB = st.columns(2)

    with colA:
        st.subheader("Revenue Over Time")
        if not daily_trends.empty:
            st.line_chart(daily_trends.set_index("date")["revenue"])
        else:
            st.write("No data available")

    with colB:
        st.subheader("Category Distribution")
        if not category_demand.empty:
            st.bar_chart(category_demand.set_index("category")["revenue"])
        else:
            st.write("No data available")

    st.divider()

    st.subheader("Top Products by Revenue")
    if not top_products.empty:
        st.dataframe(top_products)
    else:
        st.write("No data available")
