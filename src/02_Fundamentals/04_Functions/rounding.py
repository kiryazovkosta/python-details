def round_array(array):
    return [round(n) for n in array]

def main():
    numbers = [float(number) for number in input().split(" ")]
    rounded_numbers = round_array(numbers)
    print(rounded_numbers)

if __name__ == "__main__":
    main()