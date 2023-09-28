import pandas as pd

# Create a DataFrame using the corrected data
data = {
    'age': [39, 50, 38, 53],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private'],
    'education-num': [13, 13, 9, 7],
    'marital-status': ['Never Married', 'Married-civ-spouse', 'Divorced', 'Marital-civ-Spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband'],
    'race': ['White', 'White', 'White', 'White'],
    'sex': ['Male', 'Male', 'Male', 'Male'],
    'capital-gain': [2174, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40],
    'native-country': ['US', 'US', 'US', 'US'],
    'income': ['<=50K', '<=50K', '<=50K', '<=50K']
}

df = pd.DataFrame(data)

# Filter the individuals who work in the 'Private' sector and have education number greater than 10
filtered_df = df[(df['workclass'] == 'Private') & (df['education-num'] > 10)]

if filtered_df.empty:
    print("No matching individuals found.")
else:
    # Calculate the average hours worked per week for this group
    average_hours_worked = filtered_df['hours-per-week'].mean()
    print("Filtered DataFrame:")
    print(filtered_df)
    print(f"Average hours worked per week for this group: {average_hours_worked:.2f}")