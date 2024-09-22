PREMIERE_PRICE = 12.00
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5.00

screening_type = input()
rows = int(input())
columns = int(input())
income = 0.0

capacity = rows * columns
if screening_type == "Premiere":
    income = capacity * PREMIERE_PRICE
elif screening_type == "Normal":
    income = capacity * NORMAL_PRICE
elif screening_type == "Discount":
    income = capacity * DISCOUNT_PRICE

print(f"{income:.2f} leva")