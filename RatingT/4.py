import numpy as np
import matplotlib.pyplot as plt

# Constants
initial_count = 10
growth_rate_minutes = 2.5
antibiotic_effect_interval_minutes = 120
antibiotic_effect = 0.30

# Time intervals in minutes
time_intervals = np.arange(0, 720 + 1, 2.5)  # For 12 hours

# Calculate bacteria growth without antibiotic
growth_without_antibiotic = initial_count * (2 ** (time_intervals / growth_rate_minutes))

# Calculate bacteria growth with antibiotic
growth_with_antibiotic = np.copy(growth_without_antibiotic)
for i, t in enumerate(time_intervals):
    if t > 0 and t % antibiotic_effect_interval_minutes == 0:
        growth_with_antibiotic[i:] *= (1 - antibiotic_effect)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, growth_without_antibiotic, color='blue', label='Without Antibiotic')
plt.plot(time_intervals, growth_with_antibiotic, color='green', label='With Antibiotic')
plt.axhline(y=growth_with_antibiotic[-1], color='r', linestyle='--', label='Tendency Line (With Antibiotic)')

plt.title('Bacterial Growth Over Time')
plt.xlabel('Time (in minutes)')
plt.ylabel('Bacteria Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
