from collections import deque

shakes = 0
chocolates = [int(n) for n in input().split(', ')]
milk_cups = deque([int(n) for n in input().split(', ')])

while chocolates and milk_cups and shakes < 5:
    chocolate = chocolates.pop()
    cup = milk_cups.popleft()

    if chocolate <= 0 and cup <= 0:
        continue
    if chocolate <= 0:
        milk_cups.appendleft(cup)
        continue
    if cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup:
        shakes += 1
    else:
        milk_cups.append(cup)
        chocolate -= 5
        chocolates.append(chocolate)

if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    chocolates_string = ', '.join(list(map(str, chocolates)))
    print(f"Chocolate: {chocolates_string}")
else:
    print("Chocolate: empty")

if milk_cups:
    cups_string = ', '.join(list(map(str, milk_cups)))
    print(f"Milk: {cups_string}")
else:
    print("Milk: empty")
