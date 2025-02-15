occurrences = {}
text = input()

for ch in text:
    if ch not in occurrences:
        occurrences[ch] = 0
    occurrences[ch] += 1

for (key, value) in sorted(occurrences.items()):
    print(f'{key}: {value} time/s')