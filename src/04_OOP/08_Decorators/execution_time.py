import time

class exec_time:
    """
    Import the time module. Create a decorator called exec_time.
    It should calculate how much time a function needs to be executed.
    See the examples for more clarification.

    · Use the time library to start a timer
    · Execute the function
    · Stop the timer and return the result
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        s = time.time()
        result = self.func(*args, **kwargs)
        e = time.time()
        diff = e - s
        return diff

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))

@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))

@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())