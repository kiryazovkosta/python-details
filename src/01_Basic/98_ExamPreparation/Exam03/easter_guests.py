from math import ceil

guests = int(input())
budget = float(input())

cozunacs = ceil(guests / 3)
eggs = guests * 2
total = cozunacs * 4 +  eggs * 0.45
diff = budget - total
if diff >= 0:
    print(f"Lyubo bought {cozunacs} Easter bread and {eggs} eggs.\nHe has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.\nHe needs {abs(diff):.2f} lv. more.")