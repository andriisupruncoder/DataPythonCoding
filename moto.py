
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_1_vehicle_data.csv")
# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['engine_size'], df['horsepower'], c='blue', marker='o')
plt.title('Engine Size vs. Horsepower')
plt.xlabel('Engine Size (liters)')
plt.ylabel('Horsepower')
plt.grid(True)

# Annotate each point with the vehicle model
for i, txt in enumerate(df['vehicle_model']):
    plt.annotate(txt, (df['engine_size'][i], df['horsepower'][i]))

plt.show()
