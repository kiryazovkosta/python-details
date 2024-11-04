numbers = list(map(int, input().split(" ")))
count = int(input())

smallest = sorted(numbers)[:count]
for small in smallest:
    numbers.remove(small)

print(", ".join(map(str, numbers)))