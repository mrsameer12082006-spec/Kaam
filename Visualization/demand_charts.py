import streamlit as st
import matplotlib.pyplot as plt


def plot_top_products(demand_df):
    """
    Visualizes product demand using a compact bar chart.

    Expected columns:
    product_name | total_sales
    """

    st.markdown("### 📦 Product Demand")
    st.caption("Comparison of product-wise demand to identify fast and slow movers")

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(
        demand_df["product_name"],
        demand_df["total_sales"]
    )

    ax.set_xlabel("Product")
    ax.set_ylabel("Total Units Sold")
    ax.set_title("Top Selling Products", fontsize=11)

    # ---- Visual polish (safe) ----
    ax.grid(axis="y", alpha=0.3)
    ax.set_ylim(0, demand_df["total_sales"].max() * 1.1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="both", labelsize=9)
    plt.xticks(rotation=45, ha="right")

    st.pyplot(fig)
