width = int(input())
height = int(input())

parts = width * height
while parts > 0:
    text = input()
    if text == "STOP":
        break

    numbers = int(text)
    parts -= numbers

if parts >= 0:
    print(f"{parts} pieces are left.")
else:
    print(f"No more cake left! You need {abs(parts)} pieces more.")