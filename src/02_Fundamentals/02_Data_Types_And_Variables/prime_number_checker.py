def is_prime(number: int):
    if number <= 1:
        return False
    
    for n in range(2, number // 2 + 1):
        if number % n == 0:
            return False
    return True

number = int(input())
print(is_prime(number))