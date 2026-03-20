import streamlit as st
import matplotlib.pyplot as plt


def plot_sales_trend(trend_df):
    """
    Visualizes sales trend over time.

    Expected columns:
    date | total_quantity
    """

    st.markdown("### 📈 Sales Trend")
    st.caption("Daily sales movement to understand demand patterns over time")

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(
        trend_df["date"],
        trend_df["total_quantity"],
        marker="o",
        markersize=5
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Total Units Sold")
    ax.set_title("Daily Sales Trend", fontsize=11)

    # ---- Visual polish (safe) ----
    ax.grid(axis="y", alpha=0.3)
    ax.set_ylim(
        trend_df["total_quantity"].min() * 0.95,
        trend_df["total_quantity"].max() * 1.05
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="both", labelsize=9)
    plt.xticks(rotation=45)

    st.pyplot(fig)
