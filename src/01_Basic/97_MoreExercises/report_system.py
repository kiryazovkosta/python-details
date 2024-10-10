total_sum = int(input())

cash_payment = 0
card_payment = 0
cash_sum = 0
card_sum = 0
payment_count = 0
while True:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    product_price = int(command)
    if (
        (payment_count % 2 == 0 and product_price > 100) or
        (payment_count % 2 != 0 and product_price < 10)
    ):
        print("Error in transaction!")
    else:
        print("Product sold!")
        if payment_count % 2 == 0:
            cash_payment += 1
            cash_sum += product_price
        else:
            card_payment += 1
            card_sum += product_price
        if card_sum + cash_sum >= total_sum:
            print(f"Average CS: {cash_sum/cash_payment:.2f}")
            print(f"Average CC: {card_sum/card_payment:.2f}")
            break
    payment_count += 1