def is_even(number: int) -> bool:
    return number % 2 == 0

def main():
    size = int(input())
    for _ in range(size):
        num = int(input())
        if not is_even(num):
            print(f"{num} is odd!")
            return

    print("All numbers are even.")

if __name__ == "__main__":
    main()