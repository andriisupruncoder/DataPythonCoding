import pandas as pd

def generate_price_off(df):
    # Generate all combinations of two consecutive weeks with price off
    price_off_combs = []
    for i in range(9):
        for j in range(i + 1, 10):
            price_off_combs.append([1] * i + [1] * j + [0] * (9 - i - j))
    return price_off_combs

def generate_discount(df, price_off_comb):
    # Generate all combinations of discounts for the two weeks with price off
    discounts = []
    for i in range(7, 14):
        for j in range(i, 14):
            discounts.append([i, j])
    return discounts

def main():
    df = pd.DataFrame({
        "Display ActionAlley": [0, 0, 0, 0, 0, 0, 1, 0, 1],
        "Display ApparelDownSize": [0, 0, 0, 0, 0, 1, 1, 1, 0],
        "Display Table": [0, 0, 0, 0, 0, 0, 1, 1, 1],
        "Pay_flag_Last_Month": [1, 1, 1, 1, 1, 1, 1, 1, 1],
        "const": [1, 1, 1, 1, 1, 1, 1, 1, 1]
    })

    # Generate the price off column
    price_off_combs = generate_price_off(df)
    for price_off_comb in price_off_combs:
        df["Price Off"] = price_off_comb

        # Generate the discount column
        discounts = generate_discount(df, price_off_comb)
        for discount in discounts:
            df["Discount"] = discount

            # Print the output
            print(df)

if __name__ == "__main__":
    main()