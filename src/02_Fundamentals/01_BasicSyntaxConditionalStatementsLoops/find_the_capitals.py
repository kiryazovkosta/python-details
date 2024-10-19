text = input()
indexes = list()
for char, index in zip(text, range(len(text))):
    if char.isupper():
        indexes.append(index)
print(indexes)