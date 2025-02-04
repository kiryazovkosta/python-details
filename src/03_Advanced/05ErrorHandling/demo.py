class CustomError(Exception):
    pass

a = 0
b = 1
numbers = [1, 2, 3, 4 ,5]



try:
    print(a / b)
    print(numbers[6])
    raise CustomError("Something terrable will be happen")
except ZeroDivisionError:
    print("Division by zero error")
except IndexError:
    print("List index out of range")
except CustomError:
    print("custom error is raided")





