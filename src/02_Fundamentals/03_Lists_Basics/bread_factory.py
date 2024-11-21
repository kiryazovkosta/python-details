import re
import sys

energy = 100
coins = 100
is_open = True

events = input()

matches = re.findall(r"(\w+)-(\d+)", events)

for event, number in matches:
    number = int(number)

    if event == "rest":
        new_energy = number + energy
        if new_energy > 100:
            new_energy = 100
        graned_energy = new_energy - energy
        energy = new_energy
        print(f"You gained {graned_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        new_energy = energy - 30
        if new_energy < 0:
            energy += 50
            print("You had to rest!")
        else:
            coins += number
            print(f"You earned {number} coins.")
            energy = new_energy
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            sys.exit()
            
if is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")