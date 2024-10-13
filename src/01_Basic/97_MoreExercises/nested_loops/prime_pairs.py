def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for x in range(2, (number//2)+1):
        if number % x == 0:
            return False
    return True

def main() -> None:

    first = int(input())
    second = int(input())
    increment_first = int(input())
    increment_second = int(input())

    for x in range(first, first + increment_first + 1):
        for y in range(second, second + increment_second + 1):
            if is_prime(x) and is_prime(y):
                print(f"{x}{y}")

if __name__ == "__main__":
    main()