from math import ceil, floor
single_rocket_price = float(input())
rockets = int(input())
shoes = int(input())

total_price = 0.0
rockets_price = single_rocket_price * rockets
shoes_price = single_rocket_price / 6 * shoes
total_price += rockets_price + shoes_price
total_price += total_price * 0.2

print(f"Price to be paid by Djokovic {floor(total_price/8)}")
print(f"Price to be paid by sponsors {ceil(total_price * (7/8))}")