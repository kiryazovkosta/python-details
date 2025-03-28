def type_check(typeof):
    def decorator(function):
        def wrapper(*args, **kwargs):
            item = args[0]
            if not isinstance(item, typeof):
                return "Bad Type"
            return function(*args, **kwargs)
        return wrapper
    return decorator



print("#############################")
@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))

print("#############################")
@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))