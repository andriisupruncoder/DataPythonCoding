import pandas as pd

# Sample data
data = '''Index,Title,Artist,Top Genre,Year,Beats Per Minute (BPM),Energy,Danceability,Loudness (dB),Liveness,Valence,Length (Duration),Acousticness,Speechiness,Popularity
1,Sunrise,Norah Jones,adult standards,2004,157,30,53,-14,11,68,201,94,3,71
...'''  # Your actual data would go here

# Read data into DataFrame
df = pd.read_csv('Spotify_2000.csv')

# Filter for years 2000-2007
df = df[df['Year'].between(2000, 2007)]

# Calculate average energy, danceability, and popularity for each year
average_values = df.groupby('Year')[['Energy', 'Danceability', 'Popularity']].mean()

print(average_values)

# Calculate average danceability for "alternative hip hop" each year
alt_hip_hop_danceability = df[df['Top Genre'] == 'alternative hip hop'].groupby('Year')['Danceability'].mean()

print(alt_hip_hop_danceability)

# Year with highest and lowest danceability for "alternative hip hop"
year_highest_danceability = alt_hip_hop_danceability.idxmax()
year_lowest_danceability = alt_hip_hop_danceability.idxmin()

print(f"Year with highest danceability for 'alternative hip hop': {year_highest_danceability}")
print(f"Year with lowest danceability for 'alternative hip hop': {year_lowest_danceability}")

# Calculate correlation coefficient between loudness and energy
correlation = df['Loudness (dB)'].corr(df['Energy'])

print(f"Correlation between loudness and energy: {correlation:.2f}")
