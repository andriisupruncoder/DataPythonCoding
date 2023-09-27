import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("Cleaned_Laptop_Data.csv")

# Access the names and data types of the columns at positions 5, 8, and 10
selected_columns_info = df.columns[[5, 8, 10]]
column_data_types = df[selected_columns_info].dtypes

# Check for missing values in the entire dataset
missing_values = df.isnull().sum()

print("Column Names and Data Types for positions 5, 8, and 10:\n")
print(column_data_types)
print("\nMissing Values for Each Column:\n")
print(missing_values)

# To check if there are any missing values in any of the columns
if missing_values.any():
    print("\nThere are missing values in the dataset.")
else:
    print("\nThere are no missing values in the dataset.")
