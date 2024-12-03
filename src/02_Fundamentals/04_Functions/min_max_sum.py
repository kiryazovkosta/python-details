import sys
def finding(numbers):
    min = sys.maxsize
    max = -sys.maxsize
    sum = 0

    for n in numbers:
        sum += n
        min = n if n < min else min
        max = n if n > max else max
    
    return (min, max, sum)

def printing(min: int, max: int, sum: int) -> None:
    print(f"The minimum number is {min}")
    print(f"The maximum number is {max}")
    print(f"The sum number is: {sum}")

def main():
    numbers = [int(n) for n in input().split(" ")]
    min, max, sum = finding(numbers)
    printing(min, max, sum)

if __name__ == "__main__":
    main()