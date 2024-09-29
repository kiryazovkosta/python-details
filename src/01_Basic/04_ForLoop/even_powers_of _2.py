max_power = int(input())
powers = []
for power in range(0, max_power + 1):
    if power % 2 == 0:
        powers.append(2 ** power)
print(*powers, sep='\n')