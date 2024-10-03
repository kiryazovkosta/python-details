customers = int(input())

total_check = 0
for _ in range(customers):
    products_counter = 0
    check = 0
    while True:
        product = input()
        if product == "Finish":
            if products_counter % 2 == 0:
                check -= check * 0.2
            total_check += check
            print(f"You purchased {products_counter} items for {check:.2f} leva.")
            break
        elif product == "basket":
            check += 1.50
        elif product == "wreath":
            check += 3.80
        else:
            check += 7.00

        products_counter += 1

print(f"Average bill per client is: {total_check/customers:.2f} leva.")