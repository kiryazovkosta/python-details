import os

def number_to_base(n: int, base: int) -> list[int]:
    if n == 0:
        return [0]
    indexes = []
    while n:
        indexes.append(n % base)
        n //= base
    return indexes[::-1]

def validate_numbers(numbers: list[int], magic_number: int) -> bool:
    symbols = ['+', '*']
    length = len(numbers) - 1
    max_elements = len(symbols) ** length

    for number in range(max_elements):
        arr = number_to_base(number, len(symbols))
        arr = [0] * (length - len(arr)) + arr
        symbol_arr = [symbols[d] for d in arr]
        result = numbers[0]
        for index in range(1, len(numbers)):
            if symbol_arr[index - 1] == "+":
                result += numbers[index]
            else:
                result *= numbers[index]

        if result == magic_number:
            return True
    return False

def validate_with_concatenated_numbers(numbers: list[int], magic_number: int) -> bool:
    symbols = ['+', '*', '||']
    length = len(numbers) - 1
    max_elements = len(symbols) ** length

    for number in range(max_elements):
        arr = number_to_base(number, len(symbols))
        arr = [0] * (length - len(arr)) + arr
        symbol_arr = [symbols[d] for d in arr]

        result = numbers[0]
        for i in range(1, len(numbers)):
            op = symbol_arr[i - 1]
            if op == '+':
                result += numbers[i]
            elif op == '*':
                result *= numbers[i]
            elif op == '||':
                result = int(str(result) + str(numbers[i]))
        if result == magic_number:
            return True

    return False

def first(lines: list[str]) -> int:
    total_sum = 0
    for line in lines:
        items = line.split(":")
        checked_sum = int(items[0])
        numbers = [int(n) for n in items[1].strip().split()]
        if validate_numbers(numbers, checked_sum):
            total_sum += checked_sum
    return total_sum

def second(lines: list[str]) -> int:
    total_sum = 0
    for line in lines:
        items = line.split(":")
        checked_sum = int(items[0])
        numbers = [int(n) for n in items[1].strip().split()]
        if validate_with_concatenated_numbers(numbers, checked_sum):
            total_sum += checked_sum
    return total_sum

def main():
    file_path = os.path.join(os.getcwd(), "input07.txt")
    with open(file_path, "r") as input_values_file:
        file_lines: list[str] = input_values_file.readlines()
        first_result = first(file_lines)
        print(first_result)
        second_result = second(file_lines)
        print(second_result)

if __name__ == "__main__":
    main()