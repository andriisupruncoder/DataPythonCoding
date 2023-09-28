import pandas as pd
from io import StringIO
# Sample data
data = '''brand,model,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb,weight,display_size,warranty,Touchscreen,msoffice,latest_price,old_price,discount,star_rating,ratings,reviews
ASUS,VivoBook,Intel,Core i3,11th,4,DDR4,512 GB,0 GB,Windows,64-bit,0,Casual,Missing,1,No,Yes,51649,62990,18,0.0,0,0
HP,Missing,Intel,Core i3,11th,4,DDR4,512 GB,0 GB,Windows,64-bit,0,ThinNlight,Missing,1,No,Yes,47990,51165,6,4.3,1605,215
ASUS,VivoBook,Intel,Core i3,10th,4,DDR4,512 GB,0 GB,Windows,64-bit,0,Casual,Missing,1,No,No,40990,49990,18,4.4,4008,519
ASUS,Missing,Intel,Core i3,10th,4,DDR4,512 GB,0 GB,Windows,64-bit,0,ThinNlight,Missing,1,No,Yes,42990,50990,15,4.4,1869,234
ASUS,VivoBook,Intel,Core i3,11th,4,DDR4,512 GB,0 GB,Windows,64-bit,0,Casual,Missing,1,No,No,44890,56999,21,3.9,7,0
ASUS,VivoBook,Intel,Core i3,10th,4,DDR4,512 GB,0 GB,Windows,64-bit,0,Casual,Missing,1,No,No,41490,49990,17,4.4,4008,519
HP,15s,Intel,Core i3,11th,4,DDR4,512 GB,0 GB,Windows,32-bit,0,ThinNlight,Missing,1,No,No,50990,51748,1,0.0,0,0
HP,Missing,Intel,Core i3,11th,4,DDR4,512 GB,0 GB,Windows,64-bit,0,ThinNlight,Missing,1,No,Yes,48900,50000,2,4.3,1278,135'''

# Convert the string to a pandas DataFrame
df = pd.read_csv(StringIO(data))

# For each brand, count how many rows have os_bit equal to 64-bit
brand_counts = df[df['os_bit'] == '64-bit']['brand'].value_counts()

# Number of rows with discount greater than 20 and star_rating greater than 3.1
count_condition = len(df[(df['discount'] > 20) & (df['star_rating'] > 3.1)])

print(brand_counts)
print("\nNumber of rows with discount > 20 and star_rating > 3.1:", count_condition)
