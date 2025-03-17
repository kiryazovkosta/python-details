class vowels:
    VOWELS_SYMBOLS = ['a', 'o', 'u', 'e', 'i']

    # def __init__(self, text: str):
    #     self.text = text
    #     self. index = -1
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self.index += 1
    #     if self.index >= len(self.text):
    #         raise StopIteration
    #
    #     if self.text[self.index].lower() in self.VOWELS_SYMBOLS:
    #         return self.text[self.index]
    #
    #     return self.__next__()

    def __init__(self, text: str):
        self.text = text
        self.vowels = [ch for ch in text if ch.lower() in self.VOWELS_SYMBOLS]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.vowels):
            raise StopIteration
        return self.vowels[self.index]



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)