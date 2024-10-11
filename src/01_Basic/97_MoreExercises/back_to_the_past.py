money = float(input())
last_year = int(input())

ages = 18
for year in range(1800, last_year + 1):
    money -= 12000
    if year % 2 != 0:
        money -= 50 * ages
    ages += 1

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")