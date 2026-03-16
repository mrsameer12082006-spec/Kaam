import streamlit as st
from pathlib import Path
import sys


def _ensure_project_root_in_path():
    # ensure package imports work whether running from frontend/ or project root
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))


_ensure_project_root_in_path()

try:
    from Ingestion import process_inventory_file, process_sales_file
    from analytics.analytics_runner import run_analytics
except Exception:
    # last-resort relative import
    try:
        from Ingestion import process_inventory_file, process_sales_file
        from analytics.analytics_runner import run_analytics
    except Exception:
        process_inventory_file = None
        process_sales_file = None
        run_analytics = None


def show_upload():
    st.title("Upload Inventory and Sales Data")

    st.markdown("Upload CSV or Excel files for INVENTORY and SALES. Processed files will be saved in the ingestion/data/processed folder.")

    st.markdown("## Inventory File")
    inv_file = st.file_uploader("Drag & drop inventory file here", type=["csv", "xlsx"], key="inventory_uploader")
    if inv_file is not None:
        if process_inventory_file is None:
            st.error("Ingestion pipeline not available (import error).")
        else:
            try:
                cleaned = process_inventory_file(inv_file)
                st.success("Inventory file processed successfully.")
                st.dataframe(cleaned.head(10))
                # Refresh analytics
                if run_analytics:
                    st.session_state.analytics_results = run_analytics()
                    st.success("Analytics updated!")
            except Exception as e:
                st.error(f"Error processing inventory file: {e}")

    st.markdown("### Inventory Expected Columns")
    st.table({
        "Product ID": ["P001", "P002"],
        "Product Name": ["Coffee Beans", "Green Tea"],
        "Category": ["Beverages", "Beverages"],
        "Quantity On Hand": [120, 80],
        "Reorder Point": [30, 20],
        "Unit Cost": [3.50, 2.00],
        "Selling Price": [5.99, 3.99],
        "Last Purchase Date": ["2026-01-10", "2026-01-12"]
    })

    st.divider()

    st.markdown("## Sales File")
    sales_file = st.file_uploader("Drag & drop sales file here", type=["csv", "xlsx"], key="sales_uploader")
    if sales_file is not None:
        if process_sales_file is None:
            st.error("Ingestion pipeline not available (import error).")
        else:
            try:
                cleaned = process_sales_file(sales_file)
                st.success("Sales file processed successfully.")
                st.dataframe(cleaned.head(10))
                # Refresh analytics
                if run_analytics:
                    st.session_state.analytics_results = run_analytics()
                    st.success("Analytics updated!")
            except Exception as e:
                st.error(f"Error processing sales file: {e}")

    st.divider()

    st.markdown("### Sales Expected Columns")
    st.table({
        "product": ["Coffee Beans", "Green Tea"],
        "date": ["2026-01-15", "2026-01-15"],
        "quantity": [45, 30],
        "revenue": [675.0, 240.0],
        "category": ["Beverages", "Beverages"]
    })
