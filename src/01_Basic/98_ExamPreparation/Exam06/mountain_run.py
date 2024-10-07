from math import floor

record = float(input())
distance = float(input())
speed_per_meter = float(input())

time = distance * speed_per_meter
extra_time = (floor(distance / 50)) * 30
time += extra_time
if time < record:
    print(f" Yes! The new record is {time:.2f} seconds.")
else:
    print(f"No! He was {time - record:.2f} seconds slower.")