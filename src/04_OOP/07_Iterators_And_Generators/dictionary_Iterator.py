from typing import Dict

class dictionary_iter:
    def __init__(self, dictionary: Dict[int, str]):
        self.dictionary = [(key, value) for key, value in dictionary.items()]
        self.index = -1


    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.dictionary):
            raise StopIteration

        return self.dictionary[self.index]





# first test
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
# second test
result = dictionary_iter({"name": "Peter","age": 24})
for x in result:
    print(x)