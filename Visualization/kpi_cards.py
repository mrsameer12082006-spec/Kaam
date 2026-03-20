import streamlit as st

def render_kpi_cards(kpi_data: dict):
    """
    Renders KPI summary cards for inventory dashboard.

    Expected input:
    {
        'total_products': int,
        'total_sales_quantity': int,
        'top_selling_product': str,
        'low_stock_count': int
    }
    """
    
    st.markdown("### 📊 Inventory Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total Products",
            value=kpi_data.get("total_products", 0)
        )
        with col2:
            st.metric(
                label="Total Sales Quantity",
                value=kpi_data.get("total_sales_quantity", 0)
    )

    with col3:
        st.metric(
            label="Top Selling Product",
            value=kpi_data.get("top_selling_product", "N/A")
        )

    with col4:
        st.metric(
            label="Low Stock Alerts",
            value=kpi_data.get("low_stock_count", 0)
        )
