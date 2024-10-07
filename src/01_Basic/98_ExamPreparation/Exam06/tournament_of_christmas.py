from math import ceil

days = int(input())
win_days = 0
total_price = 0
for _ in range(days):
    wins = 0
    loss = 0
    price = 0
    while True:
        command = input()
        if command == "Finish":
            break

        result = input()
        if result == "win":
            wins += 1
            price += 20
        else:
            loss += 1

    if wins > loss:
        price += price * 0.1
        win_days += 1
    total_price += price

if win_days >= ceil(days/2):
    total_price += total_price * 0.2
    print(f"You won the tournament! Total raised money: {total_price:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_price:.2f}")