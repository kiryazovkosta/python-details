FIRST = 97

size = int(input())
for a in range(FIRST, FIRST + size):
    for b in range(FIRST, FIRST + size):
        for c in range(FIRST, FIRST + size):
            print(f"{chr(a)}{chr(b)}{chr(c)}")