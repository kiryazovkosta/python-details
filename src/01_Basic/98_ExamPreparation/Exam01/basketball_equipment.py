year_tax = int(input())

shoes = year_tax - year_tax * 0.4
cloths = shoes - shoes * 0.2
balls = cloths * 0.25
accessors = balls * 0.2
total = year_tax + shoes + cloths + balls + accessors
print(f"{total:.2f}")