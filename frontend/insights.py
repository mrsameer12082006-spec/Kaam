import streamlit as st
import pandas as pd

def show_insights():
    results = st.session_state.get("analytics_results", {})

    st.title("Insights")

    product_demand = results.get("product_demand", pd.DataFrame())
    kpis = results.get("kpis", {})

    # Classify products by demand
    if not product_demand.empty:
        avg_quantity = product_demand["totalQuantity"].mean()
        high_demand = len(product_demand[product_demand["totalQuantity"] > avg_quantity * 1.5])
        medium_demand = len(product_demand[(product_demand["totalQuantity"] <= avg_quantity * 1.5) & (product_demand["totalQuantity"] >= avg_quantity * 0.5)])
        low_demand = len(product_demand[product_demand["totalQuantity"] < avg_quantity * 0.5])
        critical = kpis.get("slow_moving_count", 0)
    else:
        high_demand = 0
        medium_demand = 0
        low_demand = 0
        critical = 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("High Demand", f"{high_demand}")
    col2.metric("Medium Demand", f"{medium_demand}")
    col3.metric("Low Demand", f"{low_demand}")
    col4.metric("Critical", f"{critical}")

    st.divider()

    st.subheader("Detailed Recommendations")
    if not product_demand.empty:
        top_product = kpis.get("top_selling_product", "")
        st.write(f"**Top Selling Product:** {top_product}")
        st.write("**Recommendations:**")
        st.write("- Focus inventory on high-demand products")
        st.write("- Consider promotions for low-demand items")
        st.write("- Monitor critical items closely")
    else:
        st.write("No data available for recommendations")

    st.divider()

    st.subheader("General Best Practices")
    st.write("- Maintain inventory levels above reorder points")
    st.write("- Analyze sales trends regularly")
    st.write("- Use data-driven reordering decisions")
