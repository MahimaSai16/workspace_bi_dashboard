import pandas as pd

workspace_df = pd.read_csv(r"C:\Users\DELL\Desktop\Workspace_bi_system\data\raw\workspace_details.csv")
center_df = pd.read_csv(r"C:\Users\DELL\Desktop\Workspace_bi_system\data\raw\center_space.csv")

print("Workspace Data Info:")
print(workspace_df.info())

print("\nCenter Master Data:")
print(center_df.head())

# --- Data Cleaning ---
workspace_df = workspace_df.dropna()

# Business rule validations
workspace_df = workspace_df[
    workspace_df["occupied_seats"] <= workspace_df["total_seats"]
]

workspace_df = workspace_df[
    workspace_df["daily_revenue"] >= 0
]

# --- Derived Metrics ---
workspace_df["occupancy_rate"] = (
    workspace_df["occupied_seats"] / workspace_df["total_seats"]
) * 100

workspace_df["revenue_per_seat"] = (
    workspace_df["daily_revenue"] / workspace_df["occupied_seats"]
)

print("\nCleaned Data Preview:")
print(workspace_df.head())


# Save processed data
workspace_df.to_csv(

    r"C:\Users\DELL\Desktop\Workspace_bi_system\data\processed\workspace_cleaned.csv",
    index=False
)

print("\nCleaned data saved successfully!")

