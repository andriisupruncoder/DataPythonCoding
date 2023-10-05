import pandas as pd

# Create a date/time column
df = pd.DataFrame({
    "datetime": pd.to_datetime(["2023-03-08 12:00:00", "2023-03-09 13:00:00"]),
})

# Convert the date/time column to just a date column
df["date"] = df["datetime"].dt.date

# Print the dataframe
print(df)