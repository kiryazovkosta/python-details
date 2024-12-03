def is_perfect_number(number: int):
    divisors_sum = 0
    for n in range(1, number):
        if number % n == 0:
            divisors_sum += n
    return True if divisors_sum == number else False

def main():
    number = int(input())
    is_perfect = is_perfect_number(number)
    message = "We have a perfect number!" if is_perfect else "It's not so perfect."
    print(message)

if __name__ == "__main__":
    main()