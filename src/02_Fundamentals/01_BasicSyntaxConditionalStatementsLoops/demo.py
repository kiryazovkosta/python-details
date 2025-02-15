def print_number(numbers: list[int], index: int):
    """
    
    """
    if index < len(numbers):
        print(numbers[index])
        print_number(numbers, index + 1)

def main():
    numbers = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
    print_number(numbers=numbers, index=0)

if __name__ == "__main__":
    main()