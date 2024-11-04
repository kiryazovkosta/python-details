def is_equal(g: str) -> bool:
    return g != "None"

gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        break
    parts = command.split(" ")
    if parts[0] == "OutOfStock":
        gifts = [gift if gift != parts[1] else "None" for gift in gifts]
    elif parts[0] == "JustInCase":
        gifts[-1] = parts[1]
    elif parts[0] == "Required":
        gift = parts[1]
        index = int(parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

print(" ".join(list(filter(is_equal, gifts))))

