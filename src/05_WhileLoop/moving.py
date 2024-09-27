width = int(input())
length = int(input())
height = int(input())

free_volume = width * length * height


while free_volume > 0:
    command = input()
    if command != "Done":
        break

    boxes = int(command)
    free_volume -= boxes

if free_volume > 0:
    print(f"{free_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_volume)} Cubic meters more.")