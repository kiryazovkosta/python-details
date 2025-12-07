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
    return 0

def main():
    print(f"First task: {first('Day07/test.txt')}")
    print(f"Second task: {second('Day07/test.txt')}")

if __name__ == "__main__":
    main()