import pandas as pd

df = pd.read_csv("Loan_Default.csv")

# Sorting the data first by rate_of_interest in descending order and then by loan_amount in descending order
sorted_df = df.sort_values(by=['rate_of_interest', 'loan_amount'], ascending=[False, False])

# Getting the top row
result = sorted_df.iloc[0]

print(f"The maximum loan amount with the highest rate of interest is {result['loan_amount']} with an interest rate of {result['rate_of_interest']}.")
