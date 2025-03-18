from math import sqrt

def is_prime(n: int):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def get_primes(numbers: [int]):
    for n in numbers:
        if is_prime(n):
            yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print("########################################")
print(list(get_primes([-2, 0, 0, 1, 1, 0])))