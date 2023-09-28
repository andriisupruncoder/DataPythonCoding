import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# Filter the data for males only
male_data = df[df['Gender'] == 'Male']

# Colors and markers for different BMI categories. Modify as per the unique values in your dataset.
colors = {
    "Underweight": "blue",
    "Normal weight": "green",
    "Overweight": "yellow",
    "Obesity": "red"
}

markers = {
    "Underweight": "o",
    "Normal weight": "s",
    "Overweight": "^",
    "Obesity": "D"
}

# Create the 3D scatter plot
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')

# Loop over each BMI category and plot the respective data points with the specified color and marker
for category, color in colors.items():
    mask = male_data['BMI Category'] == category
    ax.scatter(male_data[mask]['Heart Rate'], 
               male_data[mask]['Physical Activity Level'], 
               male_data[mask]['Stress Level'], 
               c=color, marker=markers[category], label=category)

# Set labels and title
ax.set_xlabel('Heart Rate', labelpad=10)
ax.set_ylabel('Physical Activity Level', labelpad=10)
ax.set_zlabel('Stress Level', labelpad=10)
ax.set_title('3D Scatter Plot of Heart Rate, Physical Activity and Stress Level for Males')
ax.legend()

# Show the plot
plt.show()
