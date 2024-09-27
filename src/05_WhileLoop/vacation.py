vacation_price = float(input())
available_funds = float(input())

spend_counter = 0
operation_days = 0

while available_funds < vacation_price:
    operation_days += 1
    operation = input()
    amount = float(input())

    if operation == "save":
        available_funds += amount
        spend_counter = 0

    else:
        spend_counter += 1
        available_funds -= amount
        if available_funds <= 0:
            available_funds = 0

        if spend_counter == 5:
            print(f"You can't save the money.\n{operation_days}")
            break

if available_funds >= vacation_price:
    print(f"You saved the money for {operation_days} days.")