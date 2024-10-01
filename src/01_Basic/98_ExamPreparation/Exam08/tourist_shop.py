budget = float(input())

products_sum = 0
products_counter = 0
while budget >= 0:
    product = input()
    if product == "Stop":
        print(f"You bought {products_counter} products for {products_sum:.2f} leva.")
        break
    else:
        price = float(input())
        products_counter += 1
        if products_counter % 3 == 0:
            price *= 0.5

        if price > budget:
            print(f"You don't have enough money!\nYou need {price-budget:.2f} leva!")
            break

        products_sum += price
        budget -= price