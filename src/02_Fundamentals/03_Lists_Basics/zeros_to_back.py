numbers = [int(number) for number in input().split(", ")]

index = 0
for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[index] = numbers[i]
        index += 1
for i in range(index, len(numbers)):
    numbers[i] = 0

print(numbers)