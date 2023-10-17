import pandas as pd

def generate_dataframe(price_off_combinations, discount_combinations):
  dataframe = pd.DataFrame()
  for price_off_combination in price_off_combinations:
    for discount_combination in discount_combinations:
      dataframe = dataframe.append({
        "Display ActionAlley": 0,
        "Display ApparelDownSize": 0,
        "Display Table": 0,
        "Pay_flag_Last_Month": 1,
        "const": 1,
        "Price Off": price_off_combination,
        "Discount": discount_combination,
      }, ignore_index=True)
  return dataframe

price_off_combinations = []
for i in range(1, 10):
  for j in range(i + 1, 10):
    price_off_combinations.append([1] * i + [0] * (9 - i) + [1] * j + [0] * (9 - j))

discount_combinations = []
for i in range(7, 14):
  for j in range(i, 14):
    discount_combinations.append([i] * 2)

dataframe = generate_dataframe(price_off_combinations, discount_combinations)
print(dataframe)