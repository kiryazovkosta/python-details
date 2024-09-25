size = int(input())

first_sum = 0
second_sum = 0
for i in range(0, size * 2):
    n = int(input())
    if i < size:
        first_sum += n
    else:
        second_sum += n

if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    print(f"No, diff = {abs(first_sum - second_sum)}")