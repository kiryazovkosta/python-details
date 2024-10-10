def average(numbers: []):
    return sum(numbers) / len(numbers)

def main():
    size = int(input())
    numbers = [0] * size
    for index in range(0, len(numbers)):
        numbers[index] = int(input())

    avg = average(numbers)
    print(f"{avg:.2f}")

if __name__ == "__main__":
    main()