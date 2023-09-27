import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.read_csv('Monkey_Pox_Cases_Worldwide.csv')

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))

# Bar colors based on 'Suspected_Cases'
colors = ['red' if s > 0 else 'blue' for s in df['Suspected_Cases']]

# Bar plot for confirmed cases
bars = ax.bar(df['Country'], df['Confirmed_Cases'], color=colors)

# Line plot for hospitalized cases
ax2 = ax.twinx()
ax2.plot(df['Country'], df['Hospitalized'], color='green', marker='o')

# Annotating bars with Travel_History_Yes count
for bar, travel_hist_yes in zip(bars, df['Travel_History_Yes']):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 50, round(travel_hist_yes, 2), ha='center', va='bottom', color='black', weight='bold')

# Setting labels and titles
ax.set_xlabel('Country', fontsize=15)
ax.set_ylabel('Confirmed Cases', fontsize=15)
ax2.set_ylabel('Hospitalized Cases', fontsize=15)
ax.set_title('Confirmed and Hospitalized Monkey Pox Cases Worldwide', fontsize=20)

# Legends
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='blue', lw=4, label='Confirmed (No Suspected Cases)'),
                   Line2D([0], [0], color='red', lw=4, label='Confirmed (With Suspected Cases)'),
                   Line2D([0], [0], color='green', lw=4, label='Hospitalized')]

ax.legend(handles=legend_elements, loc='upper left')

plt.tight_layout()
plt.show()
