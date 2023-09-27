import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

grouped = df.groupby('Occupation').agg({
    'Sleep Duration': 'mean',
    'Quality of Sleep': 'mean',
    'Stress Level': 'mean'
}).reset_index()

bar_width = 0.25
r1 = np.arange(len(grouped))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

plt.figure(figsize=(10,6))

plt.bar(r1, grouped['Sleep Duration'], color='blue', width=bar_width, edgecolor='grey', label='Sleep Duration (hours)')
plt.bar(r2, grouped['Quality of Sleep'], color='red', width=bar_width, edgecolor='grey', label='Quality of Sleep (scale 1-10)')
plt.bar(r3, grouped['Stress Level'], color='green', width=bar_width, edgecolor='grey', label='Stress Level (scale 1-10)')

plt.xlabel('Occupations', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(grouped))], grouped['Occupation'], rotation=45)
plt.ylabel('Scale Value', fontweight='bold')
plt.legend()

plt.title('Comparison of Sleep Duration, Quality, and Stress Levels by Occupation')
plt.tight_layout()
plt.show()
