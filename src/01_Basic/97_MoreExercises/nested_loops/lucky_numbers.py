number = int(input())

for n in range(1000, 10000):
    a = (n // 1000) % 10
    b = (n // 100) % 10
    c = (n // 10) % 10
    d = (n // 1) % 10

    if a == 0 or b == 0 or c == 0 or d == 0:
        continue

    if a + b == c + d:
        if number % (a + b) == 0:
            result = a * 1000 + b * 100 + c * 10 + d
            print(f"{result}", end=" ")