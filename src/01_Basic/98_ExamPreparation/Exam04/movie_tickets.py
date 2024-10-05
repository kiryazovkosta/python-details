a1 = int(input())
a2 = int(input())
n = int(input())

x3_range = n//2 - 1

for x1 in range(a1, a2):
    if x1 % 2 == 0:
        continue

    for x2 in range(1, n):
        for x3 in range(1, x3_range + 1):
            digits_sum = x1 + x2 + x3
            if digits_sum % 2 != 0:
                print(f"{chr(x1)}-{x2}{x3}{x1}")