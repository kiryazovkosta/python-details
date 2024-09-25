MIN_INT_32 = -2147483648
MAX_INT_32 = 2147483648

min_value = MAX_INT_32
max_value = MIN_INT_32

length = int(input())
for i in range(0, length):
    number = int(input())
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

print(f"Max number: {max_value}")
print(f"Min number: {min_value}")