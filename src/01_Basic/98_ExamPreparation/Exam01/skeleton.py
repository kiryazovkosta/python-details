SECONDS_IN_MINUTE = 60

control_minutes = int(input())
control_seconds = int(input())
distance = float(input())
speed_per_100_meters = int(input())

control_time = (control_minutes * SECONDS_IN_MINUTE) + control_seconds
removed_time = (distance / 120) * 2.5
my_time = ((distance / 100) * speed_per_100_meters) - removed_time

if my_time <= control_time:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {my_time:.3f}.")
else:
    print(f"No, Marin failed! He was {my_time - control_time:.3f} second slower.")