class sequence_repeat:
    def __init__(self, text: str, number: int):
        self.text = text
        self.number = number
        self.ci = -1
        self.ti = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.ci += 1
        self.ti += 1
        if self.ti == self.number:
            raise StopIteration

        if self.ci == len(self.text):
            self.ci = 0

        return self.text[self.ci]

print("\n########################")
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print("\n########################")
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')