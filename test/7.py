import pandas as pd

# Sample data
data = {
    "User ID": ["U123", "U124", "U125", "U126", "U127", "U128", "U129", "U130"],
    "Action": ["login", "view_product", "purchase", "logout", "login", "view_product", "purchase", "logout"],
    "Timestamp": ["2023-01-01T00:00:00Z", "2023-01-01T00:05:00Z", "2023-01-01T00:15:00Z", "2023-01-01T00:20:00Z", 
                 "2023-01-01T00:25:00Z", "2023-01-01T00:35:00Z", "2023-01-01T00:50:00Z", "2023-01-01T01:00:00Z"],
    "Product ID": ["N/A", "P567", "P890", "N/A", "N/A", "P123", "P456", "N/A"],
    "Session Duration (seconds)": [60, 240, 180, 30, 90, 120, 300, 45],
    "Age Group": ["18-24", "25-34", "35-44", "45-54", "55-64", "18-24", "25-34", "35-44"],
    "Region": ["North", "South-East", "West", "North-East", "South", "North-West", "Central", "South"],
    "Device Type": ["Mobile", "Desktop", "Tablet", "Mobile", "Desktop", "Mobile", "Tablet", "Mobile"]
}

df = pd.DataFrame(data)

# Basic Statistics
average_session_duration = df["Session Duration (seconds)"].mean()
median_session_duration = df["Session Duration (seconds)"].median()
mode_age_group = df["Age Group"].mode()[0]
mode_device_type = df["Device Type"].mode()[0]
mode_region = df["Region"].mode()[0]

print(f"Average session duration: {average_session_duration:.2f} seconds")
print(f"Median session duration: {median_session_duration} seconds")
print(f"Most common age group: {mode_age_group}")
print(f"Most common device type: {mode_device_type}")
print(f"Most common region: {mode_region}")
