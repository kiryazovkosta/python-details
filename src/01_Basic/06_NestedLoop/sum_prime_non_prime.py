def is_prime(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

sum_prime = 0
sum_non_prime = 0

while True:
    command = input()
    if command == "stop":
        break

    number = int(command)
    if number < 0:
        print("Number is negative.")
        continue

    if is_prime(number):
        sum_prime += number
    else:
        sum_non_prime += number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")