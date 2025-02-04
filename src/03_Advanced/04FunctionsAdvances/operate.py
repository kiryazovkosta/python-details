from functools import reduce

def operate(operator: str, *args):
    mapper = {
        "+": lambda: reduce(lambda a, b: a + b, args),
        "-": lambda: reduce(lambda a, b: a - b, args),
        "*": lambda: reduce(lambda a, b: a * b, args),
        "/": lambda: reduce(lambda a, b: a / b, args)
    }

    return mapper[operator]()

print(operate("+", 1, 2, 3))

print(operate("*", 3, 4))