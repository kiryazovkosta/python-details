import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils_functions import read_input

def first(filename: str) -> int:
    teleporter = [list(line) for line in read_input(filename)]
    tbi = {teleporter[0].index("S")}
    tachyon_beams = 0
    for rowIndex in range(1, len(teleporter)):
        indices = set([i for i, x in enumerate(teleporter[rowIndex]) if x == '^'])
        if len(indices) == 0:
            continue
        tz = tbi.intersection(indices)
        tachyon_beams += len(tz)
        tbi -= tz
        tbi.update(i - 1 for i in tz)
        tbi.update(i + 1 for i in tz)

    return tachyon_beams

def second(filename: str) -> int:
    matrix = [list(line) for line in read_input(filename)]
    paths = {matrix[0].index("S"): 1}
    
    for rowIndex in range(1, len(matrix)):
        indices = set([i for i, x in enumerate(matrix[rowIndex]) if x == '^'])
        
        if len(indices) == 0:
            continue

        new_paths = {}
        tz = set(paths.keys()).intersection(indices)
        for z in tz:
            new_paths[z - 1] = new_paths.get(z - 1, 0) + paths[z]
            new_paths[z + 1] = new_paths.get(z + 1, 0) + paths[z]
        
        for col in paths:
            if col not in tz:
                new_paths[col] = new_paths.get(col, 0) + paths[col]
        
        paths = new_paths

    return sum(paths.values())

def main():
    print(f"First task: {first('Day07/input.txt')}")
    print(f"Second task: {second('Day07/input.txt')}")

if __name__ == "__main__":
    main()