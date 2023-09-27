import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.read_csv("BoeingOrdersandDeliveries.csv")


# Filter for 737-200 models in Africa
filtered_df = df[(df['Region'] == 'Africa') & (df['Model Series'] == '737-200')]

# Group by Delivery Year and Engine and get the count of models
grouped_df = filtered_df.groupby(['Delivery Year ', 'Engine']).size().unstack().fillna(0)

# Plot the data
grouped_df.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Number of 737-200 models in Africa by Delivery Year')
plt.ylabel('Number of Models')
plt.xlabel('Delivery Year')
plt.tight_layout()
plt.show()
