import pandas as pd
import matplotlib.pyplot as plt


# Load the data
df = pd.read_csv("feedback_and_ratings.csv")

# Group the data by timestamp and calculate the average page duration for each group
grouped_df = df.groupby("Timestamp").agg({"Duration (seconds)": "mean"})

# Plot the average page duration over time
plt.plot(grouped_df.index, grouped_df["Duration (seconds)"])
plt.xlabel("Timestamp")
plt.ylabel("Average Page Duration (seconds)")
plt.title("Average Page Duration Over Time")
plt.show()
