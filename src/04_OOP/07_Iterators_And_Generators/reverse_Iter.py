class reverse_iter:
    def __init__(self, numbers: [int]):
        self.numbers = numbers
        self.current_index = len(numbers) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < 0:
            raise StopIteration()

        current = self.numbers[self.current_index]
        self.current_index -= 1
        return current



reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

