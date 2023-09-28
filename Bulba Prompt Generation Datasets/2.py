import pandas as pd
import matplotlib.pyplot as plt

# Read the Dataset
df = pd.read_csv('Loan_Default.csv')

# Extract the 'Gender' column
gender_column = df['Gender']

# Calculate the count for each gender category
gender_counts = gender_column.value_counts()

# Create a pie chart
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')

# Set a title to the chart
plt.title('Gender Distribution')

# Display the chart
plt.show()