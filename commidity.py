import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Dataset as string
data_str = '''date,oil_brent,oil_dubai,coffee_arabica,coffee_robustas,tea_columbo,tea_kolkata,tea_mombasa,sugar_eu,sugar_us,sugar_world
2023-06-01,100,90,150,120,200,180,170,190,180,170
2023-06-02,105,95,155,125,205,185,175,195,185,175
2023-06-03,110,100,160,130,210,190,180,200,190,180
2023-06-04,115,105,165,135,215,195,185,205,195,185
2023-06-05,120,110,170,140,220,200,190,210,200,190
2023-06-06,125,115,175,145,225,205,195,215,205,195
2023-06-07,130,120,180,150,230,210,200,220,210,200
2023-06-08,135,125,185,155,235,215,205,225,215,205
2023-06-09,140,130,190,160,240,220,210,230,220,210
2023-06-10,145,135,195,165,245,225,215,235,225,215
2023-06-11,150,140,200,170,250,230,220,240,230,220
2023-06-12,155,145,205,175,255,235,225,245,235,225
2023-06-13,160,150,210,180,260,240,230,250,240,230
2023-06-14,165,155,215,185,265,245,235,255,245,235
2023-06-15,170,160,220,190,270,250,240,260,250,240'''

# Convert the string to a DataFrame
df = pd.read_csv(StringIO(data_str))

# Extracting coffee_arabica and coffee_robustas columns
arabica_prices = df['coffee_arabica']
robusta_prices = df['coffee_robustas']

# Creating the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(arabica_prices, robusta_prices, c='blue', marker='o', label='Data Points')
plt.xlabel('Arabica Coffee Prices')
plt.ylabel('Robusta Coffee Prices')
plt.title('Arabica vs Robusta Coffee Prices')
plt.legend()
plt.grid(True)
plt.show()


