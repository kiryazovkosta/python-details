def is_special(n: int, s: int):
    while n > 0:
        digit = n % 10
        if digit == 0 or s % digit != 0:
            return False
        n //= 10
    return True

special = int(input())
for number in range(1111, 10000):
    if is_special(number, special):
        print(number, end=" ")