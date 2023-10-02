import matplotlib.pyplot as plt
import numpy as np

scores = np.array([2, 5, 6, 2, 7, 3, 11, 4, 5, 5, 2, 8])

q1 = np.percentile(scores, 25)
q2 = np.median(scores)
q3 = np.percentile(scores, 75)

iqr = q3 - q1

min_value = scores.min()
max_value = scores.max()

# Create the box plot
plt.boxplot([scores], vert=True, patch_artist=True)

plt.xticks([1], ["Scores"])

plt.ylabel("Score")

plt.title("Box Plot of Scores")

plt.show()