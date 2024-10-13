check_sum = int(input())

counter = 0
password = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    current = a * b + c * d
                    if current != check_sum:
                        continue

                    print(f"{a}{b}{c}{d}", end=" ")
                    counter += 1
                    if counter == 4:
                        password = a * 1000 + b * 100 + c * 10 + d

if password > 0:
    print(f"\nPassword: {password}")
elif counter > 0:
    print("\nNo!")
else:
    print("No!")