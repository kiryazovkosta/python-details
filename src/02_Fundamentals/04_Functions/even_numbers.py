is_even = lambda n: n % 2 == 0

def filter(numbers):
    even = []
    for n in numbers:
        if is_even(n):
            even.append(n)
    return even

numbers = [int(n) for n in input().split(" ")]
print(filter(numbers))