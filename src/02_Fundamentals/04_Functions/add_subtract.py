def sub_numbers(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(subtract(sub_numbers(a, b), c))

if __name__ == "__main__":
    main()