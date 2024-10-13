a = int(input())
b = int(input())
maximum =int(input())

password_counter = 0
current_a = 35
current_b = 64

for c in range(1, a + 1):
    for d in range(1, b + 1):
        password_counter += 1
        if password_counter > maximum:
            break

        current_a = 35 if current_a > 55 else current_a
        current_b = 64 if current_b > 96 else current_b
        print(f"{chr(current_a)}{chr(current_b)}{c}{d}{chr(current_b)}{chr(current_a)}", end="|")
        current_a += 1
        current_b += 1