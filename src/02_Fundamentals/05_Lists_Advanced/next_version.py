def increase_version(ver: int):
    ver += 1
    return [digit for digit in str(ver)]

def read_current_version() -> int:
    return sum([
        digit * size
        for digit, size in zip(
            [int(number) for number in input().split(".")],
            [100, 10, 1]
        )
    ])

def print_version(version: list[str]) -> None:
    print(".".join([str(digit) for digit in version]))

def main():
    version = read_current_version()
    new_version = increase_version(version)
    print_version(new_version)

if __name__ == "__main__":
    main()