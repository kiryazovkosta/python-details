def squares(n: int):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1

s = [el for el in squares(5)]
print(s)