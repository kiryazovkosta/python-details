n = int(input())
middle = int((n + 1) / 2)
stars = 2 if n % 2 == 0 else 1

for r in range (middle):
    half = (n - stars) // 2
    for _ in range(half):
        print("-", end="")
    for _ in range(stars):
        print("*", end="")
    for _ in range(half):
        print("-", end="")
    stars += 2
    print()

for _ in range (middle, n):
    print("|", end="")
    for _ in range(n - 2):
        print("*", end="")
    print("|")