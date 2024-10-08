price = float(input())
weight = float(input())
days = int(input())
bags = int(input())

if weight < 10:
    price *= 0.2
elif 10 <= weight <= 20:
    price *= 0.5

if days < 7:
    price += price * 0.4
elif 7 <= days <= 30:
    price += price * 0.15
else:
    price += price * 0.1

bags_price = bags * price
print(f"The total price of bags is: {bags_price:.2f} lv.")