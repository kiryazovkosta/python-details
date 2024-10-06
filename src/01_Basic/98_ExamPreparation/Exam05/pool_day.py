from math import ceil

peoples = int(input())
tax = float(input())
beach_chair_price = float(input())
umbrella_price = float(input())

beach_chairs = ceil(peoples * 0.75)
umbrellas = ceil(peoples / 2)
total_tax = peoples * tax + beach_chairs * beach_chair_price + umbrellas * umbrella_price
print(f"{total_tax:.2f} lv.")