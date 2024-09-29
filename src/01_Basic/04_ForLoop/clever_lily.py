ages = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_length = 0
income_money = 0
for age in range(1, ages + 1):
    if age % 2 != 0:
        toys_length += 1
    else:
        income_money += 5 * age -1

income_money += toys_length * toy_price
if income_money >= washing_machine_price:
    print(f"Yes! {income_money-washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price-income_money:.2f}")