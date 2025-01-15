max_length = -1
min_value = -1
max_value = -1

n = int(input())
for _ in range(n):
    first_items, second_items = input().split("-")
    start, end = [int(n) for n in first_items.split(',')]
    first = {n for n in range(start, end + 1)}
    start, end = [int(n) for n in second_items.split(',')]
    second = {n for n in range(start, end + 1)}
    result = first.intersection(second)
    if len(result) > max_length:
        max_length = len(result)
        min_value = min(result)
        max_value = max(result)

numbers_string = ', '.join([str(n) for n in range(min_value, max_value + 1)])
print(f'Longest intersection is [{numbers_string}] with length {max_length}')