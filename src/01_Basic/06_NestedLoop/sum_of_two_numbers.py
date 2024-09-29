start_number = int(input())
end_number = int(input())
magic_number = int(input())

is_found = False
combination_counter = 0

for x in range(start_number, end_number + 1):
    for y in range(start_number, end_number + 1):
        combination_counter += 1
        if x + y == magic_number:
            print(f"Combination N:{combination_counter} ({x} + {y} = {magic_number})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
