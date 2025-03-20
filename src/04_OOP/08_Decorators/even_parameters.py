def even_parameters(function):
    def wrapper(*args, **kwargs):
        are_even = all(isinstance(n, int) and int(n) % 2 == 0 for n in args)
        if not are_even:
            return "Please use only even numbers!"

        return function(*args, **kwargs)
    return wrapper

@even_parameters
def func():
    return "hi"

print(func())

