from math import floor, ceil

area = int(input())
grapes_per_square_meter = float(input())
sell_wine_liters = int(input())
workers = int(input())

all_grapes = area * grapes_per_square_meter
used_for_wine = all_grapes * 0.4
produced_wine_litters = used_for_wine / 2.5

if sell_wine_liters > produced_wine_litters:
    print(f"It will be a tough winter! More {floor(sell_wine_liters-produced_wine_litters)} liters wine needed.")
else:
    diff = produced_wine_litters - sell_wine_liters
    print(f"Good harvest this year! Total wine: {floor(produced_wine_litters)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(diff/workers)} liters per person.")