class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.i = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end:
            current = self.i
            self.i += 1
            return current
        else:
            raise StopIteration()


one_to_ten = custom_range(1, 10)

for num in one_to_ten:
    print(num)