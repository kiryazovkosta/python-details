import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils_functions import read_input

def first(filename: str):
    counter = 0
    index = 50

    content = read_input(filename)
    records = [(l[0], int(l[1:])) for l in content]
    for direction, steps in records:
        if direction == "L":
            steps = steps * -1

        index = (index + steps) % 100
        
        if index == 0:
            counter = counter + 1
    return counter

def second(filename: str):
    counter = 0
    index = 50

    content = read_input(filename)
    records = [(l[0], int(l[1:])) for l in content]
    for direction, steps in records:

        passes_through_zero = 0

        if direction == "R":
            if index == 0:
                passes_through_zero = steps // 100
            else:
                if steps >= (100 - index):
                    passes_through_zero = ((steps - (100 - index)) // 100) + 1
            index = (index + steps) % 100

        else:
            if index == 0:
                passes_through_zero = steps // 100
            else:
                if steps >= index:
                    passes_through_zero = ((steps - index) // 100) + 1
            index = (index - steps) % 100

        counter = counter + passes_through_zero
    return counter


def main():
    print(f"Part 1 (input.txt): {first('Day01/input.txt')}")
    print(f"Part 2 (input.txt): {second('Day01/test.txt')}")

if __name__ == "__main__":
    main()