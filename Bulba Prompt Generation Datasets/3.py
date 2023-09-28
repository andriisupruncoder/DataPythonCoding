import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Monkey_Pox_Cases_Worldwide.csv")
plt.figure(figsize=(8, 6))
plt.scatter(
    df["Confirmed_Cases"],
    df["Hospitalized"],
    s=df["Suspected_Cases"] * 0.1,
    c=df["Travel_History_Yes"] > df["Travel_History_No"],
    cmap="coolwarm",
)
plt.xlabel("Confirmed Cases")
plt.ylabel("Hospitalized")
plt.title("Scatter Plot: Confirmed Cases vs Hospitalized")
plt.colorbar(label="Travel History (Yes: True, No: False)")
plt.show()