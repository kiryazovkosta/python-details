daily_target = float(input())

income = 0
while True:
    command = input()
    if command == "closed":
        print(f"Target not reached! You need {int(daily_target - income)}lv. more.")
        break

    operation = input()

    if command == "haircut":
        if operation == "mens":
            income += 15
        elif operation == "ladies":
            income += 20
        else:
            income += 10
    else:
        if operation == "touch up":
            income += 20
        else:
            income += 30

    if income >= daily_target:
        print("You have reached your target for the day!")
        break

print(f"Earned money: {income}lv.")