def is_number_valid(input_number: int) -> str:
    if (input_number < 100 or input_number > 200) and input_number != 0:
        return "invalid"
    return ""

number = int(input())
is_valid = is_number_valid(number)
print(is_valid)