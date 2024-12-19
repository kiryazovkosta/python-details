numbers = [int(n) for n in input().split(", ")]
current_max = 10
while len(numbers) > 0:
    current_numbers = [n for n in numbers if n <= current_max]
    print(f"Group of {current_max}'s: {current_numbers}")
    numbers = [n for n in numbers if n not in current_numbers]
    current_max += 10