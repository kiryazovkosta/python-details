peoples = [0] * 5

groups = int(input())
for _ in range(groups):
    p = int(input())
    if p >= 41:
        peoples[4] += p
    elif p >= 26:
        peoples[3] += p
    elif p >= 13:
        peoples[2] += p
    elif p >= 6:
        peoples[1] += p
    else:
        peoples[0] += p

peoples_count = sum(peoples)
print(f"{peoples[0]/peoples_count * 100:.2f}%")
print(f"{peoples[1]/peoples_count * 100:.2f}%")
print(f"{peoples[2]/peoples_count * 100:.2f}%")
print(f"{peoples[3]/peoples_count * 100:.2f}%")
print(f"{peoples[4]/peoples_count * 100:.2f}%")