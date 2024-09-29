size = int(input())

odd_sum = 0
even_sum = 0
for i in range(0, size):
    n = int(input())
    if i % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

if odd_sum == even_sum:
    print(f"Yes\nSum = {odd_sum}")
else:
    print(f"No\nDiff = {abs(odd_sum - even_sum)}")
