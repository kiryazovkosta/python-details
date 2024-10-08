w = float(input())
h = float(input())

width_in_centimeters = w * 100
length_in_centimeters = h * 100

used_width = int(width_in_centimeters // 120)
used_length = int((length_in_centimeters - 100) // 70)
places = used_width * used_length - 3
print(places)