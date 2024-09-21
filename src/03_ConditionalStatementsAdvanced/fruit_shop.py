working_day_prices = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

weekend_day_prices = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday", "Sunday"]

fruit = input()
day = input()
quantity = float(input())
price = 0.00

if day in working_days:
    if fruit in working_day_prices:
        price = quantity * working_day_prices[fruit]
    else:
        price = "error"
elif day == "Saturday" or day == "Sunday":
    if fruit in weekend_day_prices:
        price = quantity * weekend_day_prices[fruit]
    else:
        price = "error"
else:
    price = "error"

if isinstance(price, float):
    print(f'{price:.2f}')
else:
    print("error")
