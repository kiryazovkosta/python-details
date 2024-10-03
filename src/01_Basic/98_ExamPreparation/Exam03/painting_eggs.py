eggs_size = input()
eggs_color = input()
batches = int(input())

price = 0
if eggs_size == "Large":
    if eggs_color == "Red":
        price = 16
    elif eggs_color == "Green":
        price = 12
    else:
        price = 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        price = 13
    elif eggs_color == "Green":
        price = 9
    else:
        price = 7
else:
    if eggs_color == "Red":
        price = 9
    elif eggs_color == "Green":
        price = 8
    else:
        price = 5

total = batches * price
total -= total * 0.35
print(f"{total:.2f} leva.")