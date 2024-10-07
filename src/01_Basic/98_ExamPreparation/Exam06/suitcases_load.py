capacity: float = float(input())

free_capacity = capacity
box_counter = 0
while True:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    box_counter += 1
    volume = float(command)
    if box_counter % 3 == 0:
        volume += volume * 0.1

    if volume > free_capacity:
        box_counter -= 1
        print("No more space!")
        break

    free_capacity -= volume

print(f"Statistic: {box_counter} suitcases loaded.")