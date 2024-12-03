INVALID_LENGTH_MESSAGE = "Password must be between 6 and 10 characters"
INVALID_LETTER_MESSAGE = "Password must consist only of letters and digits"
INVALID_DIGITS_COUNT_MESSAGE = "Password must have at least 2 digits"

def validate_length(password: str) -> bool:
    if 6 <= len(password) <= 10:
        return True
    return False

def validate_symbols(password: str) -> bool:
    for idx in range(0, len(password)):
        if not password[idx].isalpha() and not password[idx].isdigit():
            return False
    return True 

def validate_digits(password: str) -> bool:
    count = 0
    for ch in password:
        if ch.isdigit():
            count += 1
    return count >= 2

def validate(password: str):
    is_valid = True
    errors = []
    if not validate_length(password):
        is_valid = False
        errors.append(INVALID_LENGTH_MESSAGE)
    if not validate_symbols(password):
        is_valid = False
        errors.append(INVALID_LETTER_MESSAGE)
    if not validate_digits(password):
        is_valid = False
        errors.append(INVALID_DIGITS_COUNT_MESSAGE)

    return (is_valid, errors)

def main():
    password = input()
    is_valid, errors = validate(password=password)
    if is_valid:
        print("Password is valid")
    else:
        print("\n".join(errors))

if __name__ == "__main__":
    main()
