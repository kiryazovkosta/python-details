def main():
    numbers = list(map(int, input().split(", ")))
    count = int(input())
    values = [0] * count

    for i in range(0, len(numbers), count):
        for j in range(count):
            index = i + j
            if index >= len(numbers):
                break
            values[j] += numbers[index]

    print(values)

if __name__ == '__main__':
    main()
