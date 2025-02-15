def recursive_power(number: int, power: int):
    if power == 1:
        return number

    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))

print(recursive_power(10, 100))


def sum_numbers(numbers):
    if len(numbers) == 0:
        return 0

    return numbers.pop() + sum_numbers(numbers)

print(sum_numbers([1, 2, 3, 4, 5, 6, 7]))