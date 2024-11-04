def oposite(num: str) -> int:
    number = int(num)
    return number * -1

numbers = list(map(oposite, input().split(" ")))
print(numbers)