length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

total_volume = (length * width * height) / 1000
unused_volume = total_volume * (percentage / 100)
water_volume = total_volume - unused_volume
print(water_volume)