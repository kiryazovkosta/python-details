budget = float(input())
persons = int(input())
single_person_dress_price = float(input())

decor_price = budget * 0.1
if persons > 150:
    single_person_dress_price -= single_person_dress_price * 0.1

persons_price = persons * single_person_dress_price
total = decor_price + persons_price
if budget >= total:
    print(f"Action!\nWingard starts filming with {budget-total:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {total-budget:.2f} leva more.")