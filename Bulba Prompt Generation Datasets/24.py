# Import pandas library
import pandas as pd

# Read the dataset
df = pd.read_csv('ds_salaries.csv')

# Calculate the median salary for each 'employment_type' group
median_salaries = df.groupby('employment_type')['salary_in_usd'].transform('median')

# Calculate the salary deviation for each employee
df['salary_deviation'] = abs(median_salaries - df['salary_in_usd'])

# Show the updated DataFrame
print(df)