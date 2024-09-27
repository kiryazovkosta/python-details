import sys

min_number = sys.maxsize
number = input()
while number != "Stop":
    number = int(number)
    if number < min_number:
        min_number = number
    number = input()

print(min_number)