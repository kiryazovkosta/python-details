numbers = [5, 7, 11]

def is_special(num: int):
    total_sum = 0
    while num > 0:
        digit = num % 10
        num //= 10
        total_sum += digit
    
    return total_sum in numbers

def main():
    number = int(input())
    for n in range(1, number + 1):
        print(f"{n} -> {is_special(n)}")

main()