import pandas as pd

df = pd.DataFrame({
    "datetime": [
        "2023-07-31 12:00:00",
        "2023-08-01 13:00:00",
        "2023-08-02 14:00:00",
    ]
})

# Convert datetime to date
df["datetime"] = pd.to_datetime(df["datetime"])
df["date"] = df["datetime"].dt.date

# Print the DataFrame
print(df)