import pandas as pd

df = pd.read_csv("car_data.csv")

df.sort_values("engine_size", inplace=True)

car = df.iloc[0, 0]

print(car)