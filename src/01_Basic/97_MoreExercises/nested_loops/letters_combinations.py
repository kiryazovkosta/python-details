begin = input()
end = input()
skip = input()

skip_ascii = ord(skip)
counter = 0
for x in range(ord(begin), ord(end) + 1):
    for y in range(ord(begin), ord(end) + 1):
        for z in range(ord(begin), ord(end) + 1):
            if x != skip_ascii and y != skip_ascii and z != skip_ascii:
                counter += 1
                print(f"{chr(x)}{chr(y)}{chr(z)}", end= " ")

print(f"{counter}")
