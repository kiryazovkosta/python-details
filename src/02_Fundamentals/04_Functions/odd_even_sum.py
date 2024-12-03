def sum(number: int):
    odd = 0
    even = 0
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            even += digit
        else:
            odd += digit
        number //= 10

    return (odd, even)

number = int(input())
sum_of_odd_digits, sum_of_even_digits = sum(number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")