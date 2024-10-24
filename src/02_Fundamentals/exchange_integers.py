def swap(a: int, b: int):
    temp = a
    a = b
    b = temp

def print_ints(a, b):
    print(f"a = {a}")
    print(f"b = {b}")

def main():
    a = int(input())
    b = int(input())
    print("Before:")
    print_ints(a, b)
    a, b = b, a
    print("After:")
    print_ints(a, b)

if __name__ == "__main__":
    main()