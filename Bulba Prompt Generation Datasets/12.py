import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample dataset
df = pd.read_csv("world-population-by-country-2020.csv")

# Remove nan values
df.replace('N.A.', np.nan, inplace=True)
df.dropna(inplace=True)

# Cleaning the data
df['Population 2020'] = df['Population 2020'].str.replace(',', '').astype(int)
df['Net Change'] = df['Net Change'].str.replace(',', '').astype(int)
df['Migrants (net)'] = df['Migrants (net)'].str.replace(',', '').astype(float)
df['Urban Pop %'] = df['Urban Pop %'].str.replace('%', '').astype(float)
df['Med. Age'] = df['Med. Age'].astype(int)

# Filtering based on the given conditions
filtered_df = df[(df['Med. Age'] >= 28) & (df['Urban Pop %'] >= 60) | (df['Population 2020'] > 88000000)]

# Plotting
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Distribution of selected Countries')

axes[0, 0].hist(filtered_df['Population 2020'], bins=30, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Population')

axes[0, 1].hist(filtered_df['Migrants (net)'], bins=30, color='green', edgecolor='black')
axes[0, 1].set_title('Migrants (net)')

axes[1, 0].hist(filtered_df['Net Change'], bins=30, color='yellow', edgecolor='black')
axes[1, 0].set_title('Births (Net Change)')

axes[1, 1].hist(filtered_df['Urban Pop %'], bins=30, color='orange', edgecolor='black')
axes[1, 1].set_title('Urban Population %')

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()
