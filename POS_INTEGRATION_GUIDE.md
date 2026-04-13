# POS + CSV Upload Integration Guide

## System Architecture

### Two Parallel Data Entry Systems

```
┌─────────────────────────────────────────────────────────────────┐
│                    HYBRID STOCKIFY SYSTEM                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SYSTEM 1: CSV UPLOAD              SYSTEM 2: POS (BARCODE)     │
│  ═════════════════                 ════════════════════          │
│  ├─ upload.py (UI)                 ├─ pos_page.py (UI)         │
│  ├─ Ingestion pipeline             ├─ Barcode scanner          │
│  │  ├─ Load CSV files              ├─ Cart management          │
│  │  ├─ Validate schemas            ├─ Transaction handler      │
│  │  └─ Clean data                  └─ Receipt generation       │
│  └─ Save to:                        └─ Updates to:              │
│     ingestion/data/processed/          data/processed/          │
│     ├─ clean_sales.csv                ├─ stockify.db (SQLite)   │
│     └─ clean_inventory.csv            └─ Synced to CSV files    │
│                                                                 │
│              ┌──────────────────────────────────┐              │
│              │  UNIFIED DATA LAYER               │              │
│              │  data/processed/                  │              │
│              │  ├─ stockify.db (Database)       │              │
│              │  ├─ clean_sales.csv              │              │
│              │  └─ clean_inventory.csv          │              │
│              └──────────────────────────────────┘              │
│                         │                                      │
│                         ▼                                      │
│              ANALYTICS ORCHESTRATOR                           │
│              analytics_runner.py                              │
│              (reads from CSV → processes → displays)          │
│                         │                                      │
│          ┌──────────────┼──────────────┐                      │
│          ▼              ▼              ▼                      │
│     DASHBOARDS    ANALYTICS    REPORTS                       │
│     ├─ Dashboard  ├─ KPIs       ├─ Trends                  │
│     ├─ Products   ├─ Demand     ├─ Insights                │
│     ├─ POS View   ├─ Categories └─ Charts                  │
│     └─ Alerts     └─ Trends                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagrams

### Flow 1: Traditional CSV Upload (Existing)
```
User uploads CSV
    ↓
upload.py → ingestion.inventory_pipeline.process_inventory_file()
    ↓
ingestion/data/processed/inventory_cleaned.csv
    ↓
analytics_runner.run_analytics()
    ↓
Reads clean_inventory.csv
    ↓
Dashboard, Products, Insights pages display data
```

### Flow 2: Real-Time POS (New)
```
User scans barcode
    ↓
pos_page.py → barcode_scanner / product_lookup
    ↓
Add to cart (cart.py)
    ↓
User confirms sale
    ↓
pos_page → database.record_sale()
    ↓
Transaction recorded to stockify.db
    ↓
database._sync_sales_csv()
    ↓
Updates data/processed/clean_sales.csv
    ↓
Updates data/processed/clean_inventory.csv
    ↓
Analytics automatically picks up new data
    ↓
Dashboard, Products, Insights, Charts display updated data
```

### Flow 3: Unified Data After Both Operations
```
clean_sales.csv contains:
├─ Rows from uploaded CSV files
└─ Rows from POS transactions

clean_inventory.csv contains:
├─ Original inventory data
└─ Updated stock levels from POS transactions

analytics_runner reads both and displays unified view
```

---

## Files Modified for Integration

### 1. frontend/app.py ✅ MODIFIED
**Changes:**
- Added import: `from pos.pos_page import show_pos_page`
- Added page routing: `elif page == "💳 POS": show_pos_page()`

**Why:**
- Requests POS page when user clicks POS navigation button
- Keeps both systems in the same app

### 2. frontend/navigation.py ✅ MODIFIED
**Changes:**
- Added POS to pages list: `("💳", "POS")`
- Placed after Upload, before Overview

**Why:**
- Makes POS accessible from navigation
- Logical placement: Upload → POS → Analytics Views

### 3. frontend/upload.py ✅ MODIFIED
**Changes:**
- Added info banner explaining POS option
- Non-intrusive message about barcode scanning

**Why:**
- Informs users about both systems available
- Encourages real-time data entry
- No functionality broken

### 4. pos/pos_integration.py ✨ CREATED (NEW)
**Purpose:**
- Bridges POS transactions with analytics
- Ensures CSV sync after transactions
- Helper functions for data consistency

**Key Functions:**
```python
ensure_data_synced()         # Verify POS CSV sync
record_pos_sale()            # Save sale to clean_sales.csv
update_pos_inventory()       # Update stock in clean_inventory.csv
trigger_analytics_refresh()  # Signal to re-run analytics
```

---

## How Data Stays in Sync

### Sync Mechanism

The synchronization happens at three levels:

#### Level 1: POS Database (SQLite)
- File: `data/processed/stockify.db`
- Created by: `pos/database.py`
- Auto-syncs when data is written

#### Level 2: CSV Files
- `data/processed/clean_sales.csv` 
- `data/processed/clean_inventory.csv`
- Created by: Ingestion pipeline OR POS database sync
- Both upload and POS write to these same files

#### Level 3: Analytics
- File: `analytics/analytics_runner.py`
- Reads from CSV files
- Processes unified data
- Returns combined results

### Key Points

✅ **Both CSV Upload and POS write to the same CSV files**
- Upload pipeline: writes clean_sales.csv
- POS system: updates database, syncs to clean_sales.csv
- Result: Analytics reads combined data

✅ **CSV sync happens automatically**
- `pos/database.py` has `_sync_sales_csv()` method
- Called after each transaction
- Ensures clean_sales.csv is up-to-date

✅ **No data loss or conflict**
- Each row has unique transaction_id
- Append-only model (never overwrites)
- Both sources feed into same table

---

## Testing the Integration

### Test 1: Upload System Still Works
```
1. Go to Upload page
2. Upload inventory CSV
3. Upload sales CSV
4. Go to Dashboard
5. Verify metrics and charts display
→ Expected: CSV data shows correctly
```

### Test 2: POS System Works
```
1. Go to POS page
2. Enter product code (e.g., P001)
3. Add to cart
4. Complete transaction
5. Verify inventory updated
→ Expected: Stock decremented, sale recorded
```

### Test 3: Data Integration Works
```
1. Upload CSV with 10 initial sales
2. Dashboard shows those sales
3. Use POS to add 2 more transactions
4. Go to Dashboard
5. Check KPIs and trends
→ Expected: Dashboard shows 10 + 2 = 12 sales total
```

### Test 4: Bidirectional Updates
```
1. Upload sales CSV
2. Check Dashboard metrics
3. Use POS to add transactions
4. Go back to Dashboard (without refresh)
5. Check if POS data is reflected
→ Expected: If auto-refresh is enabled, new data shows
→ Otherwise: Click refresh or navigate away/back
```

---

## Navigation Structure (Updated)

```
Stockify Main Menu
├─ 🏠 Home                    [Welcome page]
├─ 📂 Upload                  [CSV upload] ← Info: "Use POS for real-time"
├─ 💳 POS                     [NEW] Barcode scanning
├─ 📊 Overview                [Dashboard - shows combined data]
├─ 📦 Products                [Product analysis]
├─ 📈 Trends                  [Time series]
├─ 💡 Insights                [Recommendations]
├─ 🚨 Alerts                  [Stock alerts]
├─ 📉 Charts                  [Visualizations]
└─ 🚪 Logout
```

---

## Critical Integration Points

### 1. Shared Data Files
```
Path: data/processed/
├─ clean_sales.csv
│  ├─ Populated by: Ingestion pipeline (from upload)
│  ├─ Updated by: POS database sync
│  └─ Read by: analytics_runner
│
├─ clean_inventory.csv
│  ├─ Populated by: Ingestion pipeline (from upload)
│  ├─ Updated by: POS inventory_update
│  └─ Read by: decision_support (for recommendations)
│
└─ stockify.db
   ├─ Created/managed by: POS system
   ├─ Synced to: clean_sales.csv and clean_inventory.csv
   └─ Read by: POS operations
```

### 2. No Conflicts
- ✅ Upload and POS don't interfere
- ✅ CSV format is compatible for both
- ✅ Each transaction has unique ID
- ✅ Timestamps prevent duplicates
- ✅ Append-only model prevents overwrites

### 3. Analytics Always Current
- analytics_runner reads from CSV
- CSV is kept in sync by both systems
- Result: Dashboard automatically shows latest data

---

## How Both Systems Work Together

### Scenario 1: CSV Upload Only
```
Monday: Upload weekly CSV
        → Dashboard updated
        → Insights generated
Tuesday-Friday: No POS used
        → Dashboard stays static
```

### Scenario 2: POS Only
```
Daily: Use POS for all sales
       → Each scan updates inventory
       → sales.csv gets new rows
       → Dashboard refreshes hourly
       → Insights adapt to daily changes
```

### Scenario 3: Hybrid (Recommended)
```
Monday: Upload historical data (past month)
        → Dashboard shows month-to-date
Tuesday-Friday: Use POS for real-time sales
        → Inventory updates immediately
        → Dashboard reflects same-day changes
        → Insights combine historical + real-time
```

---

## Benefits of This Integration

| Benefit | How |
|---------|-----|
| **Real-Time Sales** | POS updates inventory immediately |
| **Historical Analysis** | CSV upload brings in past data |
| **No Data Loss** | Both systems append to same tables |
| **Unified View** | Analytics sees combined dataset |
| **Flexibility** | Use CSV, POS, or both |
| **No Breaking Changes** | Upload system unchanged |
| **Easy to Toggle** | Just select different page |

---

## Troubleshooting

### Issue: POS data doesn't show in Dashboard
**Solution:**
1. Verify `data/processed/clean_sales.csv` exists
2. Check that POS transactions were completed
3. Refresh page (Ctrl+R) or navigate away/back
4. Check analytics logs

### Issue: Inventory mismatch
**Solution:**
1. Check both clean_inventory.csv and stockify.db
2. Verify CSV format matches expectations
3. Manually sync with: `database._sync_inventory_csv()`

### Issue: Duplicate transactions
**Solution:**
1. Each transaction has unique ID
2. Check transaction_id in clean_sales.csv
3. If duplicate, check timestamp

### Issue: Analytics not updating
**Solution:**
1. Force refresh: Navigate to different page, back to Dashboard
2. Restart Streamlit: `streamlit run app.py`
3. Check if clean_sales.csv is being updated

---

## Next Steps

1. ✅ Test CSV upload
2. ✅ Test POS barcode scanning
3. ✅ Verify dashboard shows both datasets
4. ✅ Check inventory sync
5. ✅ Monitor performance

All systems are now integrated and ready for hybrid operation!
