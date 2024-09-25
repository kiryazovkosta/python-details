import sys

max_number = -sys.maxsize
other_numbers_sum = 0

size = int(input())
for i in range(0, size):
    n = int(input())

    if n > max_number:
        max_number = n

    other_numbers_sum += n

other_numbers_sum -= max_number
if max_number == other_numbers_sum:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - other_numbers_sum)}")