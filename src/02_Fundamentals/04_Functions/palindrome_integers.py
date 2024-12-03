def is_palindrome(number: str) -> bool:
    for index in range(0, round(len(number)/2)):
        if number[index] != number[len(number) - 1 - index]:
            return False
    return True

numbers = input().split(", ")
for number in numbers:
    print(f"{is_palindrome(number)}")