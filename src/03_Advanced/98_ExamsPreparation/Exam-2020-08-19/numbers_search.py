def numbers_searching(*args):
    missing = None
    duplicates = []
    min_value = min(args)
    max_value = max(args)
    for n in range(min_value, max_value + 1):
        counter = args.count(n)
        if counter == 0:
            missing = n
        if counter > 1:
            duplicates.append(n)

    result = [missing, duplicates]
    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))