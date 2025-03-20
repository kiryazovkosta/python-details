from functools import wraps

def even_numbers(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        func_result = function(*args, **kwargs)
        return [num for num in func_result if num % 2 == 0]
    return wrapper

@even_numbers
def get_numbers(numbers):
    return numbers

@even_numbers
def get_special_numbers(numbers, other):
    other["h"] = 2
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))
print(get_special_numbers([7, 8, 9, 6, 0], {}))