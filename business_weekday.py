import pandas as pd

# Assuming the dataset file is in the same directory and named "business_weekday_sales.csv"
file_path = 'Copy of data_36_business_weekday_sales.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Calculate the correlation between CPI and sales
correlation = df['cpi'].corr(df['sales'])

# Display the correlation
print(f'The correlation between CPI and sales is: {correlation}')
