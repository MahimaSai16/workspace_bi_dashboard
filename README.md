# Workspace BI Dashboard

This project simulates a **Business Intelligence dashboard** for workspace occupancy & revenue analytics.

## Features
- Data cleaning & KPI generation using Python
- Interactive Streamlit dashboard with:
  - Total Revenue
  - Average Occupancy %
  - Revenue per Seat
  - Revenue trend over time
  - City-wise occupancy
  - Underutilized centers (<60% occupancy)
- Screenshot of dashboard included

## Tech Stack
- Python (pandas, matplotlib, seaborn)
- Streamlit for dashboard
- CSV datasets

## Folder Structure
Workspace-BI-System/
├── data/
│ ├── raw/
│ └── processed/
├── scripts/
│ ├── auto_process.py
│ └── dashboard.py
├── screenshots/
└── README.md


## Usage
1. Run `python scripts/auto_process.py` to generate cleaned dataset  
2. Run `streamlit run scripts/dashboard.py` to open the dashboard



