PALNOLETIE = 16
age = float(input())
gender = input()

if gender == 'm':
    if age >= PALNOLETIE:
        print('Mr.')
    else:
        print('Master')
else:
    if age >= PALNOLETIE:
        print('Ms.')
    else:
        print('Miss')