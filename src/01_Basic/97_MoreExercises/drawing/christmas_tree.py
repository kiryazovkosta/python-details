n = int(input())

for index in range(0, n + 1):
    for _ in range(n - index):
        print(" ", end="")
    for _ in range(index):
        print("*", end="")
    print(" | ", end="")

    for _ in range(index):
        print("*", end="")
    print(" ")
