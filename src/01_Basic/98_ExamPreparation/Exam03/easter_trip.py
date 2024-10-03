destination = input()
period = input()
nights = int(input())

price = 0
if destination == "France":
    if period == "21-23":
        price = 30
    elif period == "24-27":
        price = 35
    else:
        price = 40
elif destination == "Italy":
    if period == "21-23":
        price = 28
    elif period == "24-27":
        price = 32
    else:
        price = 39
else:
    if period == "21-23":
        price = 32
    elif period == "24-27":
        price = 37
    else:
        price = 43

print(f"Easter trip to {destination} : {nights * price:.2f} leva.")