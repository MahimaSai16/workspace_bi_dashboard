                                                   Workspace BI Dashboard

Project Overview
This project is a Business Intelligence dashboard simulating workspace occupancy and revenue analytics for a co-working company 
The goal is to demonstrate data cleaning, SQL analysis, and executive-ready dashboard creation using Python, Excel/Streamlit, and SQLite.  


Workspace_bi_system/
├── data/    # Raw and processed datasets
│ ├── raw/    # Original datasets
│ └── processed/    # Cleaned and ready-to-use datasets
├── scripts/    # Python scripts for cleaning, analysis, and dashboard
│ ├── data_cleaning.py     # Cleaning & feature engineering
│ ├── sql_queries.py    # SQL-based analytics
│ └── dashboard.py   # Streamlit dashboard
├── sql/    # SQL outputs / query files
├── screenshots/   # Screenshots of dashboard & charts
└── README.md    # Project documentation



 Tech Stack
- Python: pandas, matplotlib, seaborn, Streamlit  
- SQL: SQLite for data analysis & queries  
- Excel: Optional for dashboard creation & reporting  
- GitHub: Repository to store project files and documentation



Key Features / Highlights
- Automated Data Cleaning & Metric Generation  
  - Occupancy rate calculation  
  - Revenue per seat computation  
- SQL-based Analytics 
  - City-wise occupancy trends  
  - Monthly revenue trend analysis  
  - Identification of underutilized centers  
- Interactive Dashboard (Streamlit/Excel)  
  - KPI cards for total revenue, average occupancy, revenue per seat  
  - Line chart: revenue trend over time by city  
  - Bar chart: city-wise occupancy  
  - Underutilized centers visualization (<60% occupancy)  



How to Run

1️⃣ Using Streamlit
 cd scripts
 streamlit run dashboard.py
<img width="1920" height="1080" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/7dfb90f8-827f-46aa-8ce9-119493639686" />



Learning OutcomesS

Hands-on experience in data cleaning, analysis, and dashboard creation

Exposure to SQL, Excel, and Python for business insights

Understanding of real-world BI workflows: data processing → analysis → reporting → insights
<img width="1920" height="1080" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/905b9c7d-b5f3-49f7-8595-4e3edf75ba23" />


