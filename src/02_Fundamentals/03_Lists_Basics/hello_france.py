def valid_price(kind: str, price: float) -> bool:
    if kind == "Clothes" and price > 50.00:
        return False
    if kind == "Shoes" and price > 35.00:
        return False
    if kind == "Accessories" and price > 20.50:
        return False
    return True

kind_price_pairs = [item.split("->") for item in input().split("|")]
budget = float(input())
profit = 0
prices = []
for kind, price in kind_price_pairs:
    price = float(price)
    if price > budget or not valid_price(kind, price):
        continue
    budget -= price
    profit += price * 0.4
    price += price * 0.4
    prices.append(price)

print(" ".join(f"{p:.2f}" for p in prices))
print(f"Profit: {profit:.2f}")
print("Hello, France!") if sum(prices) + budget > 150 else print("Not enough money.")