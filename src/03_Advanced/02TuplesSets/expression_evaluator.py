from collections import deque

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

expression = input().split()
numbers = deque()

for ch in expression:
    if ch not in operations:
        numbers.append(int(ch))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            numbers.appendleft(operations[ch](first_number, second_number))

print(numbers.pop())