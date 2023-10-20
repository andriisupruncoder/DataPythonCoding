import pandas as pd
import numpy as np

# Read the Iris data from the CSV file
df = pd.read_csv("iris.csv")

# Filter for Iris-setosa
df_filtered = df[df['Species'] == 'Iris-setosa']

# Calculate the standard deviation of SepalWidthCm
standard_deviation = np.std(df_filtered["SepalWidthCm"])

# Print the standard deviation
print(standard_deviation)