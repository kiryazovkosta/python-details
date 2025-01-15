n, m = [int(n) for n in input().split()]

first = set()
second = set()

for _ in range(n):
    first.add(int(input()))

for _ in range(m):
    second.add(int(input()))

print('\n'.join(list(map(str, first.intersection(second)))))