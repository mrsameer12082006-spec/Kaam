import streamlit as st
import pandas as pd

def show_products():
    results = st.session_state.get("analytics_results", {})

    st.title("Products")

    product_demand = results.get("product_demand", pd.DataFrame())

    if not product_demand.empty:
        avg_quantity = product_demand["totalQuantity"].mean()
        high_demand = len(product_demand[product_demand["totalQuantity"] > avg_quantity * 1.5])
        medium_demand = len(product_demand[(product_demand["totalQuantity"] <= avg_quantity * 1.5) & (product_demand["totalQuantity"] >= avg_quantity * 0.5)])
        low_demand = len(product_demand[product_demand["totalQuantity"] < avg_quantity * 0.5])
    else:
        high_demand = 0
        medium_demand = 0
        low_demand = 0

    col1, col2, col3 = st.columns(3)
    col1.metric("High Demand", f"{high_demand}")
    col2.metric("Medium Demand", f"{medium_demand}")
    col3.metric("Low Demand", f"{low_demand}")

    st.divider()

    st.subheader("Product Performance")
    if not product_demand.empty:
        st.dataframe(product_demand)
    else:
        st.write("No product data available")
