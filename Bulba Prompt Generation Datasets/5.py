import pandas as pd

# Data provided
age = [39,50,38,53]
workclass = ["State-gov","Self-emp-not-inc","Private","Private"]
education_num = [13,13,9,7]
marital_status = ["Never Married","Married-civ-spouse","Divorced","Marital-civ-Spouse"]
occupation = ["Adm-clerical","Exec-managerial","Handlers-cleaners","Exec-managerial"]
relationship = ["Not-in-family","Husband","Not-in-family","husband"]
race = ["white","white","white","white"]
sex = ["Male","Male","Male","Male"]
capital_gain = [2174,0,0,0]
capital_loss = [0,0,0,0]
hours_per_week = [40,13,40,40]
native_country = ["US","US","US","US"]
income = ["<=50","<=50","<=50","<=50"]

# Creating the DataFrame
df = pd.DataFrame({
    "Age": age,
    "Workclass": workclass,
    "Education-Num": education_num,
    "Marital-Status": marital_status,
    "Occupation": occupation,
    "Relationship": relationship,
    "Race": race,
    "Sex": sex,
    "Capital-Gain": capital_gain,
    "Capital-Loss": capital_loss,
    "Hours-Per-Week": hours_per_week,
    "Native-Country": native_country,
    "Income": income
})

# Filtering data
filtered_data = df[(df['Workclass'] == 'Private') & (df['Education-Num'] > 10)]

# Calculate average hours worked per week
average_hours = filtered_data['Hours-Per-Week'].mean()

print(average_hours)
