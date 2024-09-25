A = 1
E = 2
I = 3
O = 4
U = 5

text = input()
vowels_sum = 0
for char in text:
    if char == "a":
        vowels_sum += A
    elif char == "e":
        vowels_sum += E
    elif char == "i":
        vowels_sum += I
    elif char == "o":
        vowels_sum += O
    elif char == "u":
        vowels_sum += U

print(vowels_sum)
