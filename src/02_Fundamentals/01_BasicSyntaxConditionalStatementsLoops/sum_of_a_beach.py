words = ["sand", "water", "fish", "sun"]

text = input().lower()

last = len(text) - 2
counter = 0
for i in range(0, last):
    j = i
    word = ""
    for j in range(i, i + 3):
        word += text[j]
    if word in words:
        counter += 1

    if last - i >= 2:
        j += 1
        word += text[j]
        if word in words:
            counter += 1

    if last - i >= 3:
        j += 1
        word += text[j]
        if word in words:
            counter += 1

print(counter)