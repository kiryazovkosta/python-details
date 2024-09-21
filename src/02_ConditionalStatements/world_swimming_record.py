from math import floor

record = float(input())
distance = float(input())
speed = float(input())

total_seconds = distance * speed
extra_seconds = floor(distance / 15) * 12.5
total_seconds += extra_seconds

seconds_diff = record - total_seconds
if total_seconds < record:
    print(f"Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_seconds-record:.2f} seconds slower.")