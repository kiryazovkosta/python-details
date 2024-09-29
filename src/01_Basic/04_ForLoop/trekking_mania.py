groups_length = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
total = 0
for g in range(0, groups_length):
    group_size = int(input())
    if group_size <= 5:
        p1 += group_size
    elif 6 <= group_size <= 12:
        p2 += group_size
    elif 13 <= group_size <= 25:
        p3 += group_size
    elif 26 <= group_size <= 40:
        p4 += group_size
    elif group_size >= 41:
        p5 += group_size

    total += group_size

print(f"{p1/total * 100:.2f}%")
print(f"{p2/total * 100:.2f}%")
print(f"{p3/total * 100:.2f}%")
print(f"{p4/total * 100:.2f}%")
print(f"{p5/total * 100:.2f}%")