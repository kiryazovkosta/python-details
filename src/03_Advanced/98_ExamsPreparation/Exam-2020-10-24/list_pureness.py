def best_list_pureness(*args):
    numbers = list(args[0])
    rotations = 0
    max_pureness = 0
    for index in range(len(numbers)):
        max_pureness += (index * numbers[index])

    for index in range(1, args[1] + 1):
        numbers.insert(0, numbers.pop())
        current_pureness = 0
        for idx in range(len(numbers)):
            current_pureness += (idx * numbers[idx])
        if current_pureness > max_pureness:
            max_pureness = current_pureness
            rotations = index
    return f"Best pureness {max_pureness} after {rotations} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)