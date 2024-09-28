start_number = int(input())
end_number = int(input())

for number in range(start_number, end_number + 1):
    odd_sum = 0
    even_sum = 0
    for digit_index, digit in enumerate(str(number)):
        digit = int(digit)
        if digit_index % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if odd_sum == even_sum:
        print(f"{number}", end=" ")