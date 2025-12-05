import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils_functions import read_input

def first(filename: str) -> int:
    counter = 0
    line_index = 0
    ranges = []
    lines = read_input(filename)
    for line_index in range(len(lines)):
        if lines[line_index] == '':
            break

        p = lines[line_index].split('-')
        ranges.append((int(p[0]), int(p[1])))
    
    for line_index in range(line_index + 1, len(lines)):
        number = int(lines[line_index])
        for min_value, max_value in ranges:
            if number >= min_value and number <= max_value:
                counter += 1
                break
        
    return counter

def second(filename: str) -> int:
    line_index = 0
    ranges = []
    numbers = set()
    lines = read_input(filename)
    for line_index in range(len(lines)):
        if lines[line_index] == '':
            break
        p = lines[line_index].split('-')
        ranges.append((int(p[0]), int(p[1])))

    for line_index in range(line_index + 1, len(lines)):
        numbers.add(int(lines[line_index]))

    ranges.sort()
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    return sum(end - start + 1 for start, end in merged)

def main():
    print(f"First task: {first('Day05/input.txt')}")
    print(f"Second task: {second('Day05/input.txt')}")

if __name__ == "__main__":
    main()