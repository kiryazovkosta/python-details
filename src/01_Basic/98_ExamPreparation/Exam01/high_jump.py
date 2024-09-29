maximum_target_height = int(input())

current_target_height = maximum_target_height - 30
total_jumps = 0
while current_target_height <= maximum_target_height:
    is_success = False
    for jumpIndex in range(0, 3):
        total_jumps += 1
        current_jump_height = int(input())
        if current_jump_height > current_target_height:
            is_success = True
            current_target_height += 5
            break
    if not is_success:
        print(f"Tihomir failed at {current_target_height}cm after {total_jumps} jumps.")
        break
if current_target_height > maximum_target_height:
    print(f"Tihomir succeeded, he jumped over {maximum_target_height}cm after {total_jumps} jumps.")