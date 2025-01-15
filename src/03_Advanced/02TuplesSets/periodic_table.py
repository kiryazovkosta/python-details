n = int(input())
elements = set()

for _ in range(n):
    for element in input().split():
        elements.add(element)

print('\n'.join(elements))