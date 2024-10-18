import sys

def find(divisor: int, boundary: int) -> int:
    largest = -sys.maxsize

    for n in range(divisor, boundary + 1):
        if n % divisor == 0:
            largest = n
    
    return largest

def main():
    d = int(input())
    b = int(input())
    larger = find(d, b)
    print(larger)

if __name__ == "__main__":
    main()