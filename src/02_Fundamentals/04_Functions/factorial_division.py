factorials = {}

def factorial(number: int):
    result = 1
    for n in range(1, number + 1):
        result *= n

    return result

first = int(input())
second = int(input())

print(f"{factorial(first)/factorial(second):.2f}")