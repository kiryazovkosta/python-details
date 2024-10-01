FUEL_PRICE_PER_LITER = 2.1
TOUR_GUIDE_PRICE = 100
SATURDAY_DISCOUNT = 0.1
SUNDAY_DISCOUNT = 0.2

budget = float(input())
fuel_liters = float(input())
day = input()

total_price = fuel_liters * FUEL_PRICE_PER_LITER + TOUR_GUIDE_PRICE
if day == "Saturday":
    total_price -= total_price * SATURDAY_DISCOUNT
else:
    total_price -= total_price * SUNDAY_DISCOUNT

difference = budget - total_price
if difference >= 0:
    print(f"Safari time! Money left: {difference:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(difference):.2f} lv.")