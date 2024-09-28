number = int(input())
combinations_counter = 0
for a in range(0, number + 1):
    for b in range(0, number + 1):
        for c in range(0, number + 1):
            if a + b + c == number:
                combinations_counter += 1

print(combinations_counter)
