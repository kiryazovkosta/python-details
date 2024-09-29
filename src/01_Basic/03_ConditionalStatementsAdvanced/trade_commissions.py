ERROR_MESSAGE = "error"
city = input()
sales = float(input())
commission = 0.00

if sales < 0:
    print(ERROR_MESSAGE)
else:
    if city == "Sofia":
        if sales <= 500:
            commission = sales * 0.05
        elif sales <= 1000:
            commission = sales * 0.07
        elif sales <= 10000:
            commission = sales * 0.08
        else:
            commission = sales * 0.12
    elif city == "Varna":
        if sales <= 500:
            commission = sales * 0.045
        elif sales <= 1000:
            commission = sales * 0.075
        elif sales <= 10000:
            commission = sales * 0.1
        else:
            commission = sales * 0.13
    elif city == "Plovdiv":
        if sales <= 500:
            commission = sales * 0.055
        elif sales <= 1000:
            commission = sales * 0.08
        elif sales <= 10000:
            commission = sales * 0.12
        else:
            commission = sales * 0.145
    else:
        print(ERROR_MESSAGE)

if commission != 0.00:
    print(f"{commission:.2f}")

