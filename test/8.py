import pandas as pd
from io import StringIO
# Reading the data
data = """
User ID,Action,Timestamp,Product ID,Session Duration (seconds),Age Group,Region,Device Type
U123,login,2023-01-01T00:00:00Z,N/A,60,18-24,North,Mobile
U124,view_product,2023-01-01T00:05:00Z,P567,240,25-34,South-East,Desktop
U125,purchase,2023-01-01T00:15:00Z,P890,180,35-44,West,Tablet
U126,logout,2023-01-01T00:20:00Z,N/A,30,45-54,North-East,Mobile
U127,login,2023-01-01T00:25:00Z,N/A,90,55-64,South,Desktop
U128,view_product,2023-01-01T00:35:00Z,P123,120,18-24,North-West,Mobile
U129,purchase,2023-01-01T00:50:00Z,P456,300,25-34,Central,Tablet
U130,logout,2023-01-01T01:00:00Z,N/A,45,35-44,South,Mobile
"""
df = pd.read_csv(StringIO(data))

# Identifying outliers based on session duration
outliers = df[(df['Session Duration (seconds)'] < 30) | (df['Session Duration (seconds)'] > 250)]['User ID'].tolist()

# Spotting anomalies based on action and product ID
anomalies = df[((df['Action'] == 'login') | (df['Action'] == 'logout')) & (df['Product ID'] != 'N/A')]['User ID'].tolist()

print(f"Outliers based on session duration: {outliers}")
print(f"Anomalies based on action and product ID: {anomalies}")
