from math import sqrt, prod
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils_functions import read_input

def first(filename: str) -> int:
    points = [list(map(int, p)) for p in [l.split(',') for l in read_input(filename)]]
    ordered = []
    for i in range(0, len(points) - 1):
        for j in range(i + 1, len(points)):
            current_calc = calc(points[i], points[j])
            ordered.append((current_calc, [i, j]))
    ordered.sort()
    boxes = list()
    count = 1
    for order in ordered:
        if count > 1000:
            break

        count = count + 1

        box = next((b for b in boxes if order[1][0] in b and order[1][1] in b), None)
        if box is not None:
            #print(f"{count} -> {boxes}")
            continue
        box_a: set|None = next((b for b in boxes if order[1][0] in b), None)
        box_b: set|None = next((b for b in boxes if order[1][1] in b), None)
        if box_a is None and box_b is None:
            boxes.append({order[1][0], order[1][1]})
        elif box_a is not None and box_b is not None:
            boxes.append(box_a.union(box_b))
            boxes.remove(box_a)
            boxes.remove(box_b)
        elif box_a is not None:
            box_a.add(order[1][1])
        elif box_b is not None:
            box_b.add(order[1][0])

    return prod(len(box) for box in sorted(boxes, key=len, reverse=True)[:3])

def second(filename: str) -> int:
    points = [list(map(int, p)) for p in [l.split(',') for l in read_input(filename)]]
    ordered = []
    for i in range(0, len(points) - 1):
        for j in range(i + 1, len(points)):
            current_calc = calc(points[i], points[j])
            ordered.append((current_calc, [i, j]))
    ordered.sort()
    boxes = list()
    last_cable_length = 0
    for order in ordered:
        box = next((b for b in boxes if order[1][0] in b and order[1][1] in b), None)
        if box is not None:
            continue
        box_a: set|None = next((b for b in boxes if order[1][0] in b), None)
        box_b: set|None = next((b for b in boxes if order[1][1] in b), None)
        if box_a is None and box_b is None:
            boxes.append({order[1][0], order[1][1]})
        elif box_a is not None and box_b is not None:
            boxes.append(box_a.union(box_b))
            boxes.remove(box_a)
            boxes.remove(box_b)
        elif box_a is not None:
            box_a.add(order[1][1])
        elif box_b is not None:
            box_b.add(order[1][0])

        if len(boxes[0]) == len(points):
            last_cable_length = points[order[1][0]][0] * points[order[1][1]][0]

    return last_cable_length

def calc(f: list[int], s: list[int]):
    a = abs(f[0] - s[0])
    b = abs(f[1] - s[1])
    c = abs(f[2] - s[2])
    return sqrt(a ** 2 + b ** 2 + c ** 2)

def main():
    print(f"First task: {first('Day08/input.txt')}")
    print(f"Second task: {second('Day08/input.txt')}")

if __name__ == "__main__":
    main()