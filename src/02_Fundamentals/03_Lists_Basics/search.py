size = int(input())
word = input()

sentenses = []
for _ in range(size):
    sentense = input()
    sentenses.append(sentense)
print(sentenses)

for index in range(len(sentenses) - 1, -1, -1):
    if word not in sentenses[index]:
        sentenses.remove(sentenses[index])
print(sentenses)