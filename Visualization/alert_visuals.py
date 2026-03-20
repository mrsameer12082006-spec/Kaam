import streamlit as st


def show_alerts(alert_df):
    """
    Displays inventory alerts in a compact, readable format.

    Expected columns:
    product_name | alert_type | message
    """

    st.markdown("### ⚠️ Inventory Alerts")

    if alert_df.empty:
        st.caption("No inventory alerts. Stock levels are healthy.")
        return

    for _, row in alert_df.iterrows():
        if row["alert_type"] == "LOW_STOCK":
            st.markdown(
                f"- 🔻 **{row['product_name']}**: {row['message']}"
            )
        elif row["alert_type"] == "OVERSTOCK":
            st.markdown(
                f"- 📦 **{row['product_name']}**: {row['message']}"
            )
        else:
            st.markdown(
                f"- **{row['product_name']}**: {row['message']}"
            )
