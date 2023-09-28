import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Ensure it's a square plot for a perfect circle
ax.set_aspect('equal', 'box')

# Set limits for better visualization
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)

# Colors for the circles, starting from the outermost circle
colors = ['red', 'black', 'red', 'black', 'red', 'white']

# Draw concentric circles starting from the outermost
for i, color in enumerate(reversed(colors)):
    circle = patches.Circle((0, 0), radius=6-i, fc=color)  # fc means fill color
    ax.add_patch(circle)

# Remove axis ticks and labels for clarity
ax.axis('off')

# Show the plot
plt.show()
