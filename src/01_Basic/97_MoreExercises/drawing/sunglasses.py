n = int(input())

for index in range(n):
    if index == 0 or index == n - 1:
        for _ in range(2 * n):
            print("*", end="")
        for _ in range(n):
            print(" ", end="")
        for _ in range(2 * n):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for _ in range(2 * n - 2):
            print("/", end="")
        print("*", end="")
        if index == (n-1) // 2:
            for _ in range(n):
                print("|", end="")
        else:
            for _ in range(n):
                print(" ", end="")

        print("*", end="")
        for _ in range(2 * n - 2):
            print("/", end="")
        print("*")