numbers = [int(n) for n in input().split(", ")]

positive = [n for n in numbers if n >= 0]
negative = [n for n in numbers if n < 0]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]

print(f"Positive: {', '.join([str(n) for n in positive])}")
print(f"Negative: {', '.join(list(map(str, negative)))}")
print(f"Even: {', '.join([str(n) for n in even])}")
print(f"Odd: {', '.join([str(n) for n in odd])}")