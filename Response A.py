import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv')

# Check for missing values
missing_values = df.isna().sum()
print(missing_values)

# Check for outliers
outliers = df.apply(lambda x: np.abs(x - x.mean()) > 3 * x.std(), axis=0)
print(outliers)

# Check for correlations
corr = df.corr()
print(corr)

# Plot correlations
plt.figure(figsize=(10, 10))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()