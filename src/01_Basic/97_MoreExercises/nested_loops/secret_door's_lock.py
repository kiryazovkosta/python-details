primes = [2, 3, 5, 7]
a:int = int(input())
b:int = int(input())
c:int = int(input())

for x in range(1, a + 1):
    for y in range(1, b + 1):
        for z in range(1, c + 1):
            if x % 2 != 0 or z % 2 != 0:
                continue
            if y not in primes:
                continue

            print(f"{x} {y} {z}")