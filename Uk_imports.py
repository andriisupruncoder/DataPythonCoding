import pandas as pd

# Read the dataset into a DataFrame
df = pd.read_csv("UK_imports.csv")

# Normalize monthly import values
monthly_columns = [col for col in df.columns if col not in ["COMMODITY", "COUNTRY"]]
for column in monthly_columns:
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())

# Calculate total yearly imports for each commodity and nation
yearly_columns = [str(year) + month for year in range(2018, 2023) for month in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]]
df['Yearly_Total'] = df[yearly_columns].sum(axis=1)

# Manually compute quartiles and assign labels
quartiles = df['Yearly_Total'].quantile([0, .25, .5, .75, 1]).drop_duplicates().tolist()
labels = ["Low", "Medium", "High", "Very High"]

if len(quartiles) - 1 == len(labels):
    df['Yearly_Rank'] = pd.cut(df['Yearly_Total'], bins=quartiles, labels=labels, include_lowest=True)
else:
    print("Warning: Not enough unique quartile edges. Labels may not be accurately assigned.")

# Pivot the data
pivot_columns = [str(year) for year in range(2018, 2024)]
df_melted = df.melt(id_vars=["COMMODITY", "COUNTRY"], value_vars=yearly_columns, var_name="Year_Month", value_name="Total_Imports")
df_melted['Year'] = df_melted['Year_Month'].str[:4]
df_pivot = pd.pivot_table(df_melted, index=["Year"], columns=["COUNTRY", "COMMODITY"], values="Total_Imports", aggfunc="sum").fillna(0)

# Save the final DataFrame to a new CSV file
df_pivot.to_csv("UK_imports_transformed.csv")

print("Data transformation completed. Check the 'UK_imports_transformed.csv' file.")
