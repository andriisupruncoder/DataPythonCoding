import pandas as pd
import numpy as np

# Load the dataset from the CSV file
file_path = 'AAPL.csv'
df = pd.read_csv(file_path)

# Extract the year and month from the date and create new columns for each
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month

# Apply Min-Max normalization on 'open' and 'close' columns
min_open, max_open = df['open'].min(), df['open'].max()
min_close, max_close = df['close'].min(), df['close'].max()
df['normalized_open'] = (df['open'] - min_open) / (max_open - min_open)
df['normalized_close'] = (df['close'] - min_close) / (max_close - min_close)

# Create a new column with bin of volume
df['volume_bin'] = pd.cut(df['volume'], bins=np.linspace(df['volume'].min(), df['volume'].max(), 11), labels=False)

# Save the modified DataFrame back to a new CSV file
df.to_csv('Modified_AAPL.csv', index=False)

print("Modifications have been applied and saved in 'Modified_AAPL.csv'.")
