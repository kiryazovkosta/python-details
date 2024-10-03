eggs = int(input())

sold_eggs = 0
while True:
    command = input()
    if command == "Close":
        print(f"Store is closed!\n{sold_eggs} eggs sold.")
        break
    else:
        quantity = int(input())
        if command == "Fill":
            eggs += quantity
        else:
            if quantity > eggs:
                print(f"Not enough eggs in store!\nYou can buy only {eggs}.")
                break
            eggs -= quantity
            sold_eggs += quantity