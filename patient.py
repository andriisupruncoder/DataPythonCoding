# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Initialize the dataset as a string
dataset_str = '''patient_id,age_years,gender,weight_pounds,height_inches,body_mass_index,case_number,follow_up_time_in_days,outcome
1,45,male,180,72,25,12345,30,good
2,30,female,120,60,20,45678,15,bad
3,50,male,200,78,30,78901,20,good
4,25,female,100,50,15,23456,10,bad
5,60,male,220,86,35,98765,25,good'''

# Convert the string dataset to a pandas DataFrame
df = pd.read_csv(StringIO(dataset_str))

# Plot the distribution of genders
gender_distribution = df['gender'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(gender_distribution.index, gender_distribution.values, color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Number of Patients')
plt.title('Distribution of Genders in the Patient Details Spreadsheet')
plt.show()