import sys

pairs = int(input())

previous_result = -sys.maxsize
max_diff_result = -sys.maxsize
are_equal = True

for _ in range(pairs):
    a = int(input())
    b = int(input())
    result = a + b

    if previous_result != -sys.maxsize:
        diff = abs(result - previous_result)
        if diff != 0:
            are_equal = False

        if diff > max_diff_result:
            max_diff_result = diff

    previous_result = result

if are_equal:
    print(f"Yes, value={previous_result}")
else:
    print(f"No, maxdiff={max_diff_result}")