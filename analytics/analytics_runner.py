import sys
import os
from pathlib import Path
_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

"""
Analytics Runner Module

This module loads processed data from ingestion and runs all analytics functions.
"""

import pandas as pd
from pathlib import Path
import sys
import os

# Ensure we can import from analytics and Ingestion
# Support both local dev (parent dir) and Vercel (flat deployment)
project_dir = Path(__file__).resolve().parent
project_root = Path(__file__).resolve().parents[1]
for p in [str(project_dir), str(project_root)]:
    if p not in sys.path:
        sys.path.insert(0, p)

from analytics.demand_analysis import aggregate_product_demand, aggregate_category_demand, aggregate_top_products
from analytics.trend_analysis import aggregate_daily_trends
from analytics.kpi_calculator import compute_kpi_summary
from decision_support.recommendations import generate_recommendations

def load_processed_data():
    """
    Load processed inventory and sales data from ingestion/data/processed/
    Checks multiple paths for compatibility with local dev and Vercel.
    """
    # Try multiple possible locations for processed data
    possible_dirs = [
        project_dir / "data" / "processed",
        project_root / "Ingestion" / "data" / "processed",
    ]
    
    processed_dir = None
    for d in possible_dirs:
        if d.exists():
            processed_dir = d
            break
    
    if processed_dir is None:
        processed_dir = possible_dirs[0]  # fallback

    sales_file = processed_dir / "sales_cleaned.csv"
    inventory_file = processed_dir / "inventory_cleaned.csv"

    sales_df = None
    inventory_df = None

    if sales_file.exists():
        sales_df = pd.read_csv(sales_file)
        print(f"Loaded sales data: {sales_df.shape}")

    if inventory_file.exists():
        inventory_df = pd.read_csv(inventory_file)
        print(f"Loaded inventory data: {inventory_df.shape}")

    return sales_df, inventory_df

def run_analytics():
    """
    Run all analytics on the processed data.
    Returns a dictionary with all results.
    """
    sales_df, inventory_df = load_processed_data()

    results = {}

    if sales_df is not None and not sales_df.empty:
        # Run demand analysis
        results['product_demand'] = aggregate_product_demand(sales_df)
        results['category_demand'] = aggregate_category_demand(sales_df)
        results['top_products'] = aggregate_top_products(sales_df, top_n=10)
        results['daily_trends'] = aggregate_daily_trends(sales_df)
        results['kpis'] = compute_kpi_summary(sales_df)
    else:
        # Default empty results
        results['product_demand'] = pd.DataFrame()
        results['category_demand'] = pd.DataFrame()
        results['top_products'] = pd.DataFrame()
        results['daily_trends'] = pd.DataFrame()
        results['kpis'] = {
            "total_products": 0,
            "total_sales_quantity": 0,
            "top_selling_product": "",
            "slow_moving_count": 0
        }

    # Decision Support: stock alerts + reorder recommendations
    if inventory_df is not None and not inventory_df.empty:
        try:
            results['stock_recommendations'] = generate_recommendations(inventory_df)
        except Exception as e:
            print(f"Warning: Decision support failed: {e}")
            results['stock_recommendations'] = pd.DataFrame()
    else:
        results['stock_recommendations'] = pd.DataFrame()

    results['inventory_df'] = inventory_df
    results['sales_df'] = sales_df

    return results

if __name__ == "__main__":
    # For testing
    results = run_analytics()
    print("Analytics completed.")
    print(f"KPIs: {results['kpis']}")
    if not results['stock_recommendations'].empty:
        print(f"Stock Recommendations: {results['stock_recommendations'].shape[0]} products")
