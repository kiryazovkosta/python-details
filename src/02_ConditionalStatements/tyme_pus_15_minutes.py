hours = int(input())
minutes = int(input())
minutes += 15

minutes_at_end = minutes % 60
total_hours  = hours + minutes // 60
hours_at_end = total_hours if total_hours < 24 else 0

print(f'{hours_at_end}:{minutes_at_end:02d}')