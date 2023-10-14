import seaborn as sns

# Create a DataFrame with distinct (month,year) pairs
df_xy = resampled.drop_duplicates(subset=['month', 'year'])

# Plot the line plot
sns.lineplot(x='month', y='count_views', hue='channel_cat', data=df_xy)

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Count Views')
plt.title('Count Views by Channel Category')

# Show the plot
plt.show()