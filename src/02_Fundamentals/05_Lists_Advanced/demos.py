numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd = [number ** 2 for number in numbers if number % 2 != 0 and number * -1 < -5]

print(odd)


sub = [num * 2 if num % 2 == 0 else num / 3 for num in numbers]
print(sub, end="\n")

vowels = ['a','o','u','e','i']
text = "Cartesian product using a list comprehension"
filtered = [char for char in text if char.lower() not in vowels]
print(''.join(filtered))