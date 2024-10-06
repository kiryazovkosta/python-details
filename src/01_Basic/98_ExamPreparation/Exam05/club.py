wanted_income = float(input())
total_income = 0
while total_income < wanted_income:
    cocktail = input()
    if cocktail == "Party!":
        print(f"We need {wanted_income-total_income:.2f} leva more.")
        break
    cocktails_number = int(input())
    cocktails_price = len(cocktail) * cocktails_number
    if cocktails_price % 2 != 0:
        cocktails_price -= cocktails_price * 0.25
    total_income += cocktails_price
    if total_income >= wanted_income:
        print("Target acquired.")
        break

print(f"Club income - {total_income:.2f} leva.")