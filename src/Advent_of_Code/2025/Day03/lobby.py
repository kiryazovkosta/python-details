import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils_functions import read_input

def find(filename: str, size: int) -> int:
    return sum([largest_digits_joltage(bank, size) for bank in read_input(filename)])

def largest_digits_joltage(bank: str, size: int) -> int:
    previous_max_index = -1
    digits = []
    for index in range(1, size + 1):
        max_joltage = -1
        max_joltage_index = -1
        length = len(bank) - size + index
        for i in range(previous_max_index + 1, length):
            current = int(bank[i])
            if current > max_joltage:
                max_joltage = current
                max_joltage_index = i

        previous_max_index = max_joltage_index
        digits.append(max_joltage)
    return int("".join(map(str, digits)))

def main():
    print(f"First task: {find('Day03/input.txt', 2)}")
    print(f"Second task: {find('Day03/input.txt', 12)}")

if __name__ == "__main__":
    main()