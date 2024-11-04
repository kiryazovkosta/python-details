factor = int(input())
count = int(input())

numbers = []
for index in range(1, count + 1):
    numbers.append(factor * index)

print(numbers)