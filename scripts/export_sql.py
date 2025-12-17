import sqlite3
import pandas as pd
import os

# --- paths ---
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "sql", "bi_project.db")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "processed", "sql_outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- connect to sqlite ---
conn = sqlite3.connect(DB_PATH)

# ------------------ QUERY 1 ------------------
q1 = """
SELECT 
ROUND(SUM(occupied_seats) * 100.0 / SUM(total_seats), 2) AS occupancy_rate
FROM workspace_cleaned;
"""
df1 = pd.read_sql_query(q1, conn)
df1.to_csv(os.path.join(OUTPUT_DIR, "occupancy_overall.csv"), index=False)

# ------------------ QUERY 2 ------------------
q2 = """
SELECT 
city,
SUM(daily_revenue) AS total_revenue,
ROUND(AVG(occupancy_rate), 2) AS avg_occupancy
FROM workspace_cleaned
GROUP BY city;
"""
df2 = pd.read_sql_query(q2, conn)
df2.to_csv(os.path.join(OUTPUT_DIR, "city_revenue_occupancy.csv"), index=False)

# ------------------ QUERY 3 ------------------
q3 = """
SELECT 
center_id,
ROUND(AVG(occupancy_rate), 2) AS avg_occupancy
FROM workspace_cleaned
GROUP BY center_id
HAVING avg_occupancy < 60;
"""
df3 = pd.read_sql_query(q3, conn)
df3.to_csv(os.path.join(OUTPUT_DIR, "underutilized_centers.csv"), index=False)

# ------------------ QUERY 4 ------------------
q4 = """
SELECT 
SUBSTR(date,1,7) AS month,
SUM(daily_revenue) AS revenue
FROM workspace_cleaned
GROUP BY month
ORDER BY month;
"""
df4 = pd.read_sql_query(q4, conn)
df4.to_csv(os.path.join(OUTPUT_DIR, "monthly_revenue.csv"), index=False)

# ------------------ QUERY 5 ------------------
q5 = """
SELECT 
center_id,
SUM(daily_revenue) AS total_revenue
FROM workspace_cleaned
GROUP BY center_id
ORDER BY total_revenue DESC
LIMIT 5;
"""
df5 = pd.read_sql_query(q5, conn)
df5.to_csv(os.path.join(OUTPUT_DIR, "top_revenue_centers.csv"), index=False)

conn.close()

print("✅ SQL results exported to CSV successfully")
