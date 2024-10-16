def is_between(num: float) -> bool:
    return 1 <= num <= 100

def main():
    num = 0.0
    while not is_between(num):
        num = float(input())
    print(f"The number {num} is between 1 and 100")

if __name__ == "__main__":
    main()