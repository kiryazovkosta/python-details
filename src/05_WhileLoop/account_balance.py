balance = 0.0
income = input()

while income != "NoMoreMoney":
    income = float(income)
    if income >= 0:
        balance += income
        print(f"Increase: {income:.2f}")
        income = input()
    else:
        print("Invalid operation!")
        break

print(f"Total: {balance:.2f}")