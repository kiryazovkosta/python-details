from collections import deque

def main():
    worms = [int(w) for w in input().split()]
    holes = deque([int(h) for h in input().split()])

    worms_count = len(worms)
    matches = 0
    while worms and holes:
        worm = worms[-1]
        hole = holes[0]
        if worm <= 0:
            worms.pop()
            continue

        if worm == hole:
            matches += 1
            worms.pop()
            holes.popleft()
        else:
            holes.popleft()
            worms[-1] -= 3

    if matches > 0:
        print(f"Matches: {matches}")
    else:
        print("There are no matches.")


    if worms:
        print(f"Worms left: {', '.join(map(str, worms))}")
    elif worms_count > matches:
        print("Worms left: none")
    else:
        print("Every worm found a suitable hole!")

    if holes:
        print(f"Holes left: {', '.join(map(str, holes))}")
    else:
        print("Holes left: none")


if __name__ == "__main__":
    main()
