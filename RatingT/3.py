import matplotlib.pyplot as plt
import numpy as np

# Constants
initial_bacteria = 10  # Initial number of bacteria
growth_rate = 2.0  # Doubling every 2.5 minutes
antibiotic_reduction_rate = 0.3  # Reducing by 30% every 2 hours
time_span_minutes = 600  # Total time span in minutes
time_intervals = np.arange(0, time_span_minutes + 1, 5)  # Time intervals in minutes

# Calculate the number of bacteria without antibiotic
bacteria_no_antibiotic = [initial_bacteria * (2 ** (t / 2.5)) for t in time_intervals]

# Calculate the number of bacteria with antibiotic
bacteria_with_antibiotic = [initial_bacteria]
for t in range(5, time_span_minutes + 1, 5):
    hours = t / 60
    reduction_factor = (1 - antibiotic_reduction_rate) ** (hours / 2)
    bacteria_with_antibiotic.append(bacteria_with_antibiotic[-1] * reduction_factor)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, bacteria_no_antibiotic, label='Without Antibiotic', color='blue')
plt.plot(time_intervals, bacteria_with_antibiotic, label='With Antibiotic', color='red')

# Calculate and plot the tendency line (linear regression)
tendency_x = np.array(time_intervals)
tendency_y = np.log2(bacteria_no_antibiotic)
coefficients = np.polyfit(tendency_x, tendency_y, 1)
tendency_line = 2 ** (coefficients[1] + coefficients[0] * tendency_x)
plt.plot(time_intervals, tendency_line, linestyle='--', color='green', label='Tendency Line')

# Set plot labels and legend
plt.xlabel('Time (minutes)')
plt.ylabel('Number of Bacteria')
plt.title('Bacteria Growth with and Without Antibiotic')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()