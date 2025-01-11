from collections import deque

liters = int(input())
names = deque([])

name = input()
while name != "Start":
    names.append(name)
    name = input()

command = input()
while command != "End":
    if command.startswith("refill"):
        liters += int(command.split(" ")[1])
    else:
        wanted_liters = int(command)
        if names:
            name = names.popleft()
            if wanted_liters <= liters:
                liters -= wanted_liters
                print(f"{name} got water")
            else:
                print(f"{name} must wait")
    command = input()

print(f"{liters} liters left")    