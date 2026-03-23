import pandas as pd


def generate_stock_alerts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate inventory health alerts based on stock levels and cost structure.

    Expected columns:
    - Product Name
    - Quantity On Hand
    - Reorder Point
    - Unit Cost
    - Selling Price
    """

    required_cols = {
        "Product Name",
        "Quantity On Hand",
        "Reorder Point",
        "Unit Cost",
        "Selling Price"
    }

    if not required_cols.issubset(df.columns):
        raise ValueError("Inventory DataFrame missing required columns.")

    alerts = []

    for _, row in df.iterrows():
        product = row["Product Name"]
        stock = row["Quantity On Hand"]
        reorder_point = row["Reorder Point"]
        unit_cost = row["Unit Cost"]
        selling_price = row["Selling Price"]

        stock_value = stock * unit_cost
        potential_revenue = stock * selling_price
        profit_margin = (
            ((selling_price - unit_cost) / selling_price) * 100
            if selling_price > 0 else 0
        )

        # ----------------------------
        # Alert Logic
        # ----------------------------

        if stock <= reorder_point:
            alert_type = "Low Stock"
            risk_level = "High"
            recommendation = "Reorder immediately to avoid stock-out."

        elif stock > reorder_point * 3:
            alert_type = "Overstock"
            risk_level = "Medium"
            recommendation = "Reduce next purchase or consider promotional discount."

        else:
            alert_type = "Healthy"
            risk_level = "Low"
            recommendation = "Stock level is optimal."

        alerts.append({
            "Product Name": product,
            "Current Stock": stock,
            "Reorder Point": reorder_point,
            "Alert Type": alert_type,
            "Risk Level": risk_level,
            "Stock Value": round(stock_value, 2),
            "Potential Revenue": round(potential_revenue, 2),
            "Profit Margin (%)": round(profit_margin, 2),
            "Recommendation": recommendation
        })

    return pd.DataFrame(alerts)


import streamlit as st

def show_stock_alerts():
    """
    Streamlit page component to display inventory alerts.
    """
    st.markdown('<div class="page-title">🚨 Inventory Alerts</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Actionable alerts for your current inventory levels</div>',
        unsafe_allow_html=True,
    )

    results = st.session_state.get("analytics_results", {})
    stock_recs = results.get("stock_recommendations", pd.DataFrame())

    if not stock_recs.empty:
        st.dataframe(stock_recs, use_container_width=True)
    else:
        st.markdown("""
        <div class="glass-card" style="text-align:center; padding:56px 20px;">
            <div style="font-size:56px; margin-bottom:16px; filter:drop-shadow(0 0 16px rgba(50,121,249,0.15));">📭</div>
            <div style="font-size:20px; font-weight:700; color:#121317; margin-bottom:8px;">No Alerts Generated</div>
            <div style="font-size:14px; color:#9AA0A6; max-width:400px; margin:0 auto;">
                Upload inventory and sales CSV files to generate actionable stock alerts.
            </div>
        </div>
        """, unsafe_allow_html=True)
