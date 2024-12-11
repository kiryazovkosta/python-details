def sign(a: int, b: int, c: int) -> str:
    numbers = [a, b, c]
    if 0 in numbers:
        return "zero"
    if all(n > 0 for n in numbers):
        return "positive"
    elif all(n < 0 for n in numbers) < 0:
        return "negative"
    else:
        count = sum(1 for number in numbers if number < 0)
        return "negative" if count % 2 != 0 else "positive"

a = int(input())
b = int(input())
c = int(input())

print(sign(a, b, c))