import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils_functions import read_input

def first(filename: str) -> int:
    counter = 0
    wall = [list(l) for l in read_input(filename)]
    for row_index in range(len(wall)):
        for col_index in range(len(wall[row_index])):
            if wall[row_index][col_index] == "@" and paper_in_adjacent_positions(row_index, col_index, wall):
                counter += 1
    return counter

def second(filename: str) -> int:
    counter_total = 0
    wall = [list(l) for l in read_input(filename)]
    counter_current = -1
    while counter_current != 0:
        counter_current = 0
        for row_index in range(len(wall)):
            for col_index in range(len(wall[row_index])):
                if wall[row_index][col_index] == "@" and remove_paper_in_adjacent_positions(row_index, col_index, wall):
                    counter_current += 1
        counter_total += counter_current
    
    return counter_total

def paper_in_adjacent_positions(row: int, col: int, wall) -> bool:
    counter = 0
    for r in range(row - 1, row + 1 + 1):
        for c in range(col - 1, col + 1 + 1):
            if r >= 0 and c >= 0 and r < len(wall) and c < len(wall[col]):
                if wall[r][c] == "@" and (r != row or c != col):
                    counter += 1
    return counter < 4

def remove_paper_in_adjacent_positions(row: int, col: int, wall) -> bool:
    canBeRemoved = paper_in_adjacent_positions(row, col, wall)
    wall[row][col] = '.' if canBeRemoved else '@'
    return canBeRemoved

def main():
    print(f"First task: {first('Day04/input.txt')}")
    print(f"Second task: {second('Day04/input.txt')}")

if __name__ == "__main__":
    main()