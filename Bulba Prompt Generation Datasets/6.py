import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Gender': ['Sex Not Available', 'Male', 'Male', 'Male', 'Joint', 'Joint', 'Joint', 'Female', 'Joint', 'Sex Not Available',
               'Male', 'Sex Not Available', 'Joint', 'Joint', 'Female', 'Male', 'Joint', 'Male', 'Female'],
    'Credit_Score': [758, 552, 834, 587, 602, 864, 860, 863, 580, 788, 723, 501, 884, 520, 773, 685, 846, 534, 629]
}

df = pd.DataFrame(data)

# Create a histogram for 'Credit_Score' by applicant gender
plt.figure(figsize=(8, 6))
plt.hist(df[df['Gender'] == 'Sex Not Available']['Credit_Score'], bins=10, alpha=0.7, label='Sex Not Available', color='blue')
plt.hist(df[df['Gender'] == 'Male']['Credit_Score'], bins=10, alpha=0.7, label='Male', color='green')
plt.hist(df[df['Gender'] == 'Joint']['Credit_Score'], bins=10, alpha=0.7, label='Joint', color='red')
plt.hist(df[df['Gender'] == 'Female']['Credit_Score'], bins=10, alpha=0.7, label='Female', color='purple')

plt.xlabel('Credit Score')
plt.ylabel('Frequency')
plt.title('Credit Score Distribution by Applicant Gender')
plt.legend()
plt.grid(True)

# Show the histogram
plt.show()