def fibonacci():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f + s

generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))