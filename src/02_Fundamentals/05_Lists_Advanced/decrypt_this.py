words = [word for word in input().split(" ")]
for word in words:
    first_symbol = chr(int(''.join([n for n in word if n.isdigit()])))
    letters = [char for char in word if char.isalpha()]
    letters[0], letters[-1] = letters[-1], letters[0]
    print(f"{first_symbol}{''.join(letters)}", end=" ")