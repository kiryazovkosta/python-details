import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils_functions import read_input

def first(filename: str) -> int:
    total = 0
    equations = [[x for x in val.split(" ") if x] for val in read_input(filename)]
    for col_index in range(0, len(equations[0])):
        current = 0
        operation = None
        for row_index in range(len(equations) - 1, -1, -1):
            if operation == None:
                operation = equations[row_index][col_index]
                current = 0 if operation == "+" else 1
            else:
                number = int(equations[row_index][col_index])
                current = current + number if operation == "+" else current * number
        total += current
    return total

def second(filename: str) -> int:
    total = 0
    equations = [line.replace('\n', '') for line in read_input(filename, False)]
    operations = [x for x in equations[len(equations) - 1].split(" ") if x]
    cols_length = max(len(x) for x in equations)
    equations = [x.ljust(cols_length) for x in equations]
    current = []
    operation_index = len(operations) - 1

    for col_index in range(len(equations[0]) - 1, -1, -1):
        current_string = ''

        for row_index in range(0, len(equations) - 1):
            current_string += equations[row_index][col_index]

        if not current_string.isspace():
            current.append(int(current_string.strip()))

        if col_index == 0 or current_string.isspace():
            if len(current) > 0:
                operation = operations[operation_index]
                if operation == "+":
                    current_sum = 0
                    for n in current:
                        current_sum += n
                else:
                    current_sum = 1
                    for n in current:
                        current_sum *= n
                total += current_sum
                operation_index -= 1
            current.clear()

    return total

def main():
    print(f"First task: {first('Day06/input.txt')}")
    print(f"Second task: {second('Day06/input.txt')}")

if __name__ == "__main__":
    main()