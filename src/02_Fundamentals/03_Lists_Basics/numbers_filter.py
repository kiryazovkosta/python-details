size = int(input())

numbers = []
for _ in range(size):
    numbers.append(int(input()))

command = input()
result = []
for number in numbers:
    if command == "even":
        if number % 2 == 0:
            result.append(number)
    elif command == "odd":
        if number % 2 != 0:
            result.append(number)
    elif command == "negative":
        if number < 0:
            result.append(number)
    elif command == "positive":
        if number >= 0:
            result.append(number)
print(result)