from collections import deque

bees = deque(int(b) for b in input().split())
nectar = [int(n) for n in input().split()]
symbols = deque(input().split())

honey = 0

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey += abs(operators[symbols.popleft()](bees.popleft(), nectar.pop()))
    else:
        nectar.pop()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(n) for n in nectar])}")