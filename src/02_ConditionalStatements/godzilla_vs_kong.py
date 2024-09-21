budget = float(input())
statists_count = int(input())
clothes_price_per_statist = float(input())

decore_price = budget * 0.1

if statists_count > 150:
    clothes_price_per_statist = clothes_price_per_statist - (clothes_price_per_statist * 0.1)
clothes_price = statists_count * clothes_price_per_statist

total = budget - (decore_price + clothes_price)
if total >= 0:
    print("Action!")
    print(f"Wingard starts filming with {total:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(total):.2f} leva more.")