def draw_top(size: int) -> None:
    for i in range(1, size + 1):
        for _ in range(0, i):
            print("*", end="")
        print()

def draw_bottom(size: int) -> None:
    for i in range(size - 1, 0, -1):
        for _ in range(0, i):
            print("*", end="")
        print()

def main():
    count = int(input())
    draw_top(count)
    draw_bottom(count)

if __name__ == "__main__":
    main()



