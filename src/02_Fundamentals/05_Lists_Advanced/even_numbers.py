numbers = list(map(int, input().split(", ")))

found = map(
    lambda x: x if numbers[x] % 2 == 0 else -1, 
    range(len(numbers))
)

print(list(filter(lambda i: i != -1, found)))