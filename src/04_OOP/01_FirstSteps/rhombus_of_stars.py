def print_rhombus(n: int):
    print_top(n)
    print_bottom(n)

def print_top(n: int):
    for index in range(n + 1):
        print(" " *(n - index), end="")
        for _ in range(index):
            print("*", end = " ")
        print()

def print_bottom(n: int):
    for index in range(n - 1, -1, -1):
        print(" " * (n - index), end="")
        for _ in range(index):
            print("*", end=" ")
        print()


def main():
    number = int(input())
    print_rhombus(number)

if __name__ == "__main__":
    main()