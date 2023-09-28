import matplotlib.pyplot as plt

# Data
titles = ["Eminem - Walk On Water (Audio) ft. Beyoncé", "PLUSH - Bad Unboxing Fan Mail", "Racist Superman | Rudy Mancuso, King Bach & Lele Pons", 
          "I Dare You: GOING BALD!?", "Ed Sheeran - Perfect (Official Music Video)", "Jake Paul Says Alissa Violet CHEATED with LOGAN PAUL! #DramaAlert Team 10 vs Martinez Twins!"]

likes = [787425, 127794, 146035, 132239, 1634130, 103755]
dislikes = [43420, 1688, 5339, 1989, 21082, 4613]

# Calculate like-to-dislike ratio
like_to_dislike_ratio = [l/d for l, d in zip(likes, dislikes)]

# Create a larger figure to accommodate the labels
plt.figure(figsize=(12, 8))

# First subplot for dislikes
plt.subplot(2, 1, 1)
plt.bar(titles, dislikes, color='red')
plt.ylabel('Dislikes')
plt.xticks(rotation=45, ha="right")

# Second subplot for like-to-dislike ratio
plt.subplot(2, 1, 2)
plt.bar(titles, like_to_dislike_ratio, color='green')
plt.ylabel('Like-to-Dislike Ratio')
plt.xticks(rotation=45, ha="right")

# Adjust space between the subplots
plt.subplots_adjust(hspace=0.5)

# Show plot
plt.show()
