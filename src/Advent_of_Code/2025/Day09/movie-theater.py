import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils_functions import read_input

def first(filename: str) -> int:
    max_area = 0
    points = [tuple([int(l) for l in line.split(",")]) for line in read_input(filename)]
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            current_area = calc_area(points[i], points[j])
            if current_area > max_area:
                max_area = current_area
    return max_area

def second(filename: str) -> int:
    return 0

def calc_area(a: tuple, b: tuple):
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)

def main():
    print(f"First task: {first('Day09/input.txt')}")
    print(f"Second task: {second('Day09/test.txt')}")

if __name__ == "__main__":
    main()