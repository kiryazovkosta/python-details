numbers = tuple([float(n) for n in input().split()])

records = {}
for element in numbers:
    records[element] = numbers.count(element)
    #records[element] = 1 if element not in records else records[element] + 1

for key, value in records.items():
    print(f"{key:.1f} - {value} times")