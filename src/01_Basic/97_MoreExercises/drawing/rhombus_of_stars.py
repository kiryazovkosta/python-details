size = int(input())

for index in range(1, size + 1):
    for _ in range(size - index):
        print(" ", end= "")
    print("*", end="")

    for _ in range(index - 1):
        print(" *", end="")
    print()

for index in range(size - 1, 0, -1):
    for _ in range(size - index - 1):
        print(" ", end="")
    for _ in range(index):
        print(" *", end="")
    print()
