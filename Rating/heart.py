import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("heart_02.csv")

# Get the column names
column_names = df.columns.tolist()

# Get the last column name
last_column_name = column_names[-1]

# Print the last column name
print(last_column_name)