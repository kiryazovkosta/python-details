one = int(input())
two = int(input())
five = int(input())
matched_sum = int(input())

for x in range(0, one + 1):
    for y in range(0, two + 1):
        for z in range(0, five + 1):
            current_sum = x * 1 + y * 2 + z * 5
            if current_sum == matched_sum:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {matched_sum} lv.")