import pandas as pd

# Create the DataFrame
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Occupation': ['Scientist', 'Scientist', 'Scientist', 'Scientist', '_______', 'Teacher', 'Teacher', 'Teacher', 'Engineer', 'Engineer'],
    'Annual_Income': [19114.12, 19114.12, 19114.12, 19114.12, 34847.84, 34847.84, 34847.84, 34847.84, 143162.64, 143162.64]
}

df = pd.DataFrame(data)

# Group by 'Occupation' and calculate the mean for 'Annual_Income'
average_income = df.groupby('Occupation')['Annual_Income'].mean()

# Extract the values for Scientist and Teacher
scientist_avg_income = average_income.get('Scientist', 'Not found')
teacher_avg_income = average_income.get('Teacher', 'Not found')

print(f"Average income for a Scientist: {scientist_avg_income}")
print(f"Average income for a Teacher: {teacher_avg_income}")
