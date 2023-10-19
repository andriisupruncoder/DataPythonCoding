import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("shell_measurements.csv")

# Get the minimum viscera weight
min_viscera_weight = df["Viscera Weight (g)"].min()

# Print the minimum viscera weight
print(min_viscera_weight)