def genrange(s: int, e: int):
    for index in range(s, e  +1):
        yield index

print(list(genrange(1, 10)))