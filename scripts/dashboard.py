import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Load cleaned data ---
# Automatically get the path relative to this script
script_dir = os.path.dirname(__file__)
data_path = os.path.join(script_dir, "../data/processed/workspace_cleaned.csv")

df = pd.read_csv(data_path)

# --- Streamlit page setup ---
st.set_page_config(page_title="Workspace BI Dashboard", layout="wide")
st.title("🏢 Workspace BI Dashboard")

# --- KPIs ---
total_revenue = df['daily_revenue'].sum()
avg_occupancy = df['occupancy_rate'].mean()
revenue_per_seat = df['revenue_per_seat'].mean()

st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Average Occupancy %", f"{avg_occupancy:.2f}%")
col3.metric("Revenue per Seat", f"₹{revenue_per_seat:.2f}")

# --- Revenue Trend ---
st.subheader("Revenue Trend Over Time")
fig, ax = plt.subplots(figsize=(10,4))
sns.lineplot(data=df, x='date', y='daily_revenue', hue='city', marker='o', ax=ax)
plt.xticks(rotation=45)
plt.ylabel("Daily Revenue (₹)")
plt.xlabel("Date")
plt.legend(title="City")
st.pyplot(fig)

# --- City-wise Occupancy ---
st.subheader("City-wise Average Occupancy")
city_occupancy = df.groupby('city')['occupancy_rate'].mean().reset_index()
fig2, ax2 = plt.subplots(figsize=(8,4))
sns.barplot(data=city_occupancy, x='city', y='occupancy_rate', palette="viridis", ax=ax2)
plt.ylabel("Average Occupancy %")
plt.xlabel("City")
st.pyplot(fig2)

# --- Underutilized Centers ---
st.subheader("Underutilized Centers (<60% occupancy)")
underutilized = df[df['occupancy_rate'] < 60]
if underutilized.empty:
    st.write("No centers under 60% occupancy 🎉")
else:
    fig3, ax3 = plt.subplots(figsize=(8,4))
    sns.barplot(data=underutilized, x='center_id', y='occupancy_rate', palette="magma", ax=ax3)
    plt.ylabel("Occupancy %")
    plt.xlabel("Center ID")
    st.pyplot(fig3)

